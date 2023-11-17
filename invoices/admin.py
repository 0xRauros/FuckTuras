from django.contrib import admin
from .models import Invoice, InvoiceItem, Customer


class CustomerAdmin(admin.ModelAdmin):
    pass

class InvoiceItemInline(admin.TabularInline):
    model = InvoiceItem
    

class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'user',
                    'customer', 'issuer_legal_number',
                    'concept', 'slug', 'issue_date',
                    'created', 'updated', 'iban', 'irpf']
    list_filter = ['created', 'updated']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [InvoiceItemInline]

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Invoice, InvoiceAdmin)


