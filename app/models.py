from itertools import product
from django.db import models
from django.contrib.auth.models import User

PRODUCT_TYPE_CHOICES = (
    ('suitings', 'SUITINGS'),
    ('shirtings', 'SHIRTINGS'),
    ('khadi', 'KHADI'),
    ('colorkhadi', 'COLORKHADI'),
    ('linen', 'LINEN'),
)
FABRIC_TYPE_CHOICES = (
    ('alpha', 'ALPHA'),
    ('magic', 'MAGIC'),
    ('bsy', 'BSY'),
    ('cotton', 'COTTON'),
)
DESIGN_CHOICES = (
    ('print', 'PRINT'),
    ('checks', 'CHECKS'),
    ('plane', 'PLANE'),
)

COLOR_CHART_CHOICES = (
    ('sober', 'SOBER'),
    ('fancy', 'FANCY'),
    ('white', 'WHITE'),
    ('light', 'LIGHT'),
    ('dark', 'DARK'),
)

STATUS_CHOICE = {
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On the way', 'On the way'),
    ('Delivered', 'Delivered'),
    ('Cancel', 'Cancel'),
}

COMPANY_CHOICE = {
    ('saras', 'Saras'),
    ('navkar', 'Navkar'),
    ('optimum', 'Optimum'),
    ('zplus', 'Zplus'),
    ('raymond', 'Raymond'),
    ('donear', 'Donear'),
    ('srikot', 'Srikot'),
    ('damodar', 'Damodar'),
    ('divinetouch', 'Divine-Touch'),



}


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zipcode = models.IntegerField()

    def __str__(self):
        return str(self.id)


class Product(models.Model):
    product_type = models.CharField(
        max_length=15, choices=PRODUCT_TYPE_CHOICES, default='khadi')
    price_range = models.IntegerField()
    product_name = models.CharField(max_length=70)
    fabric_type = models.CharField(
        max_length=15, choices=FABRIC_TYPE_CHOICES, default='magic')
    design = models.CharField(
        max_length=15, choices=DESIGN_CHOICES, default='plane')
    color_chart = models.CharField(
        max_length=15, choices=COLOR_CHART_CHOICES, default='sober')
    product_image = models.ImageField(upload_to='productimage')
    company = models.CharField(
        max_length=70, choices=COMPANY_CHOICE, default='saras')
    priority = models.BooleanField(default=False)
    available = models.BooleanField(default=True)


class Cart(models.Model):
    quantity = models.PositiveIntegerField(default=1)
    # prod_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    status = models.CharField(
        max_length=70, choices=STATUS_CHOICE, default='Pending')
    ordered_date = models.DateTimeField(auto_now_add=True)
