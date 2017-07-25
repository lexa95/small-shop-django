from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

STATUS = (
    ("Пол.", "Получено", ),
    ("Обр.", "Обработано", ),
    ("Отп.", "Отправлено", ),
)


class Product(models.Model):

    name = models.CharField(max_length=150, verbose_name="Название")
    slug = models.SlugField(unique=True, verbose_name="URL")
    description = models.TextField(max_length=500, verbose_name="Описание", blank=True)
    price = models.IntegerField(verbose_name="Стоимость")
    photo = models.ImageField(verbose_name="Фото")

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

        ordering = ['-id']

    def __str__(self):
        return self.name

    def _get_unique_slug(self):
        unique_slug = slugify(self.name)
        num = 1
        while Article.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save()


class Delivery(models.Model):

    name = models.CharField(max_length=150, verbose_name="Название")
    price = models.IntegerField(verbose_name="Стоимость")
    delivery_period = models.CharField(max_length=50, verbose_name="Ориентировочное время доставки")

    class Meta:
        verbose_name = 'Доставка'
        verbose_name_plural = 'Доставки'

    def __str__(self):
        return "{name} | {price} руб.".format(name=self.name, price=self.price)


class Order(models.Model):

    product = models.ForeignKey(Product, verbose_name="Товар")
    count_product = models.IntegerField(verbose_name="Кол-во товара",
                                        default=1, validators=[MinValueValidator(1), MaxValueValidator(50)])
    delivery = models.ForeignKey(Delivery, verbose_name="Доставка")
    status = models.CharField(max_length=20, choices=STATUS, default=STATUS[0][0], verbose_name='Статус')
    name_client = models.CharField(max_length=150, verbose_name="Имя клиента")
    phone_client = models.CharField(max_length=150, verbose_name="Телефон клиента")
    adress_client = models.CharField(max_length=250, verbose_name="Адрес клиента")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

        ordering = ['-date_created']

    def __str__(self):
        return "Продукт: {product}, Кол-во: {count_product}".format(
            product=self.product, count_product=self.count_product)
