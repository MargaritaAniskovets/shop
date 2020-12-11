from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
User = get_user_model()
settings.AUTH_USER_MODEL

# Catrgory
# Product
# CartProduct
# Cart
# Order
# ***
# Customer
# Specification
class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название категории')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category,verbose_name='Категория',on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Наименование продукта')
    slug = models.SlugField(unique=True)
    image = models.ImageField(verbose_name='Изображение')
    description = models.TextField(verbose_name='Описание', null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2,verbose_name='Цена')

    def __str__(self):
        return self.title

class CartProduct(models.Model):
    user = models.ForeignKey('Customer',verbose_name='Покупатель',on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart',verbose_name='Корзина',on_delete=models.CASCADE)
    product = models.ForeignKey(Product,verbose_name='Товар',on_delete=models.CASCADE)
    qty = models.PositiveBigIntegerField(default=1)
    final_price = models.DecimalField(max_digits=9, decimal_places=2,verbose_name='Общая цена')

    def __str__(self):
        return 'Продукт: {}(для корзины)'.format(self.product.title)

class Cart(models.Model):
    owner = models.ForeignKey('Customer',verbose_name='Владелец',on_delete=models.CASCADE)
    products = models.ManyToManyField(Product,blank=True)
    total_products = models.PositiveBigIntegerField(default=0)
    final_price = models.DecimalField(max_digits=9, decimal_places=2,verbose_name='Общая цена')

    def __str__(self):
        return str(self.id)

class Customer(models.Model):
    user = models.ForeignKey(User,verbose_name='Пользователь',on_delete=models.CASCADE)
    phone = models.CharField(max_length=20,verbose_name='Номер телефона')
    address = models.CharField(max_length=255,verbose_name='Адрес')

    def __str__(self):
        return 'Покупатель: {}{}'.format(self.user.first_name,self.user.last_name)

class Specifications(models.Model):

    content_type = models.ForeignKey(ContentType,on_delete=models.CASCADE)
    object_id = models.PositiveBigIntegerField()
    name = models.CharField(max_length=255,verbose_name='Имя товара для характеристик')

    def __str__(self):
        return 'Характеристики для товара: {}{}'.format(self.name)

