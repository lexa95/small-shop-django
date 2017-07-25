from django.forms import ModelForm
from .models import Order


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['count_product', 'delivery', 'name_client', 'phone_client', 'adress_client', ]
        labels = {
            "adress_client": "Адресс",
            "phone_client": "Номер телефона",
            "name_client": "Имя",
        }
