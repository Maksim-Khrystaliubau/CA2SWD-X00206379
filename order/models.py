from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from vouchers.models import Voucher
from shop.models import Product
from decimal import Decimal

class Order(models.Model):
    token = models.CharField(max_length=250, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Euro Order Total', null=True, blank=True)
    emailAddress = models.EmailField(max_length=250, blank=True, verbose_name='Email Address')
    created = models.DateTimeField(auto_now_add=True)
    billingName = models.CharField(max_length=250, null=True, blank=True)
    billingAddress1 = models.CharField(max_length=250, null=True, blank=True)
    billingCity = models.CharField(max_length=250, null=True, blank=True)
    billingPostcode = models.CharField(max_length=10, null=True, blank=True)
    billingCountry = models.CharField(max_length=200, null=True, blank=True)
    shippingName = models.CharField(max_length=250, null=True, blank=True)
    shippingAddress1 = models.CharField(max_length=250, null=True, blank=True)
    shippingCity = models.CharField(max_length=250, null=True, blank=True)
    shippingPostcode = models.CharField(max_length=10, null=True, blank=True)
    shippingCountry = models.CharField(max_length=200, null=True, blank=True)

    voucher = models.ForeignKey(
        Voucher,
        related_name='orders',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    discount = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ]
    )

    class Meta:
        db_table = 'Order'
        ordering = ['-created']

    def __str__(self):
        return str(self.id)

    def calculate_total(self):
    # Calculate the total based on OrderItem instances associated with this order
        order_items = self.orderitem_set.all()
        total = sum(item.sub_total() for item in order_items)
        # Apply discount and update the total
        discount_amount = Decimal(self.discount) / 100 * total
        total -= discount_amount
        self.total = total
        self.save()

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Product')
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Euro Price')
    order = models.ForeignKey('Order', on_delete=models.CASCADE, verbose_name='Order')

    class Meta:
        db_table = 'OrderItem'

    def sub_total(self):
        return self.quantity * self.price

    def __str__(self):
        return str(self.product)