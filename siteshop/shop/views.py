from django.shortcuts import render
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Product, Order
from django.http import Http404
from .forms import OrderForm
from django.views.generic.base import TemplateView
from django.shortcuts import redirect


def views_list_product(request):
    product_list = Product.objects.all()
    paginator = Paginator(product_list, 5)

    page = request.GET.get('page', 1)

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, 'shop/products.html', {'products': products, }, RequestContext(request))


def views_product(request, slug):
    try:
        product = Product.objects.get(slug=slug)
    except Product.DoesNotExist:
        raise Http404("Product does not exist")

    return render(request, 'shop/product.html', {'product': product, }, RequestContext(request))


def views_order(request, slug):

    try:
        product = Product.objects.get(slug=slug)
    except Product.DoesNotExist:
        raise Http404("Product does not exist")

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = Order()

            order.count_product = form.cleaned_data['count_product']
            order.delivery = form.cleaned_data['delivery']
            order.name_client = form.cleaned_data['name_client']
            order.phone_client = form.cleaned_data['phone_client']
            order.adress_client = form.cleaned_data['adress_client']
            order.product = product

            order.save()
            return redirect("shop:order-seccuss")
    else:
        form = OrderForm()

    return render(request, 'shop/order.html',
                  {'form': form, 'product': product}, RequestContext(request))


class SuccessOrder(TemplateView):
    template_name = 'shop/success_order.html'
