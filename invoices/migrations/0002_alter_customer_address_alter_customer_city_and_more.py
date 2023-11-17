# Generated by Django 4.2.6 on 2023-10-23 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='customer',
            name='city',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='customer',
            name='legal_number',
            field=models.CharField(blank=True, help_text='CIF/DNI/NIF or other identification number for the invoice customer.', max_length=40),
        ),
        migrations.AlterField(
            model_name='customer',
            name='postal_code',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
