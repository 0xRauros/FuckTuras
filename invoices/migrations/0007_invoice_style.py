# Generated by Django 4.2.6 on 2023-11-02 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0006_alter_invoice_issue_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='style',
            field=models.CharField(default='style_01', max_length=1),
        ),
    ]
