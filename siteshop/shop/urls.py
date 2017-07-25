from django.conf.urls import url
from .views import views_product, views_list_product, views_order, SuccessOrder


app_name = 'shop'

urlpatterns = [
    url(r'^products/$', views_list_product, name="products"),
    url(r'^product/(?P<slug>[\w-]+)/$', views_product, name="product"),
    url(r'^order/(?P<slug>[\w-]+)/$', views_order, name="order"),
    url(r'^order-seccuss/$', SuccessOrder.as_view(), name='order-seccuss'),
]
