# Generated by Django 4.2.6 on 2023-10-26 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0003_invoice_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='phone',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='customer',
            name='website',
            field=models.URLField(blank=True),
        ),
    ]