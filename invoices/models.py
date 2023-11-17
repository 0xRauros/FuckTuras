from django.db import models
from django.utils import timezone
from django.conf import settings


class InvoiceStyles():
    DEFAULT = 'style_01'
    STYLE_2 = 'style_02'
    STYLE_3 = 'style_03'
    STYLE_4 = 'style_04'
    STYLE_5 = 'style_05'


class Customer(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(blank=True, max_length=250)
    legal_number = models.CharField(blank=True, max_length=40, help_text='CIF/DNI/NIF or other identification number for the invoice customer.')
    postal_code = models.CharField(blank=True, max_length=20)
    city = models.CharField(blank=True, max_length=100)
    email = models.EmailField(blank=True)
    phone = models.CharField(blank=True, max_length=25)
    website = models.URLField(blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.name}'


class Invoice(models.Model):
    title = models.CharField(max_length=250)
    style = models.CharField(max_length=20, default=InvoiceStyles.DEFAULT)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='invoices',
                             on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,
                                 related_name='invoices',
                                 on_delete=models.CASCADE)
    issuer_legal_number = models.CharField(max_length=40, help_text="CIF/DNI/NIF or other identification number for the invoice issuer.")
    concept = models.TextField(help_text='Concept of the invoice. Printed in the pdf.')
    slug = models.SlugField(max_length=250)
    description = models.TextField(blank=True, help_text='Short description about the invoice for the user. Not printed in the pdf.')
    issue_date = models.DateField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    iban = models.CharField(blank=True, max_length=100, help_text='Optional bank account.')
    irpf = models.PositiveIntegerField(blank=True, default=0, help_text='Retención IRPF (campo opcional).')

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created'])
        ]

    def __str__(self):
        return f'{self.title}'
    
    def get_total_cost(self):
        return sum([item.get_cost() for item in self.items.all()])



class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice,
                                related_name='items',
                                on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    iva =  models.PositiveBigIntegerField(blank=True, default=21)

    def __str__(self):
        return str(self.id)
    
    def get_cost(self):
        return self.price * self.quantity
