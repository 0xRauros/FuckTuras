# Generated by Django 4.2.6 on 2023-11-03 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0007_invoice_style'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='style',
            field=models.CharField(default='style_01', max_length=20),
        ),
    ]