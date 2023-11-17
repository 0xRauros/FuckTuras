from django.urls import path
from . import views

app_name='invoices'

urlpatterns = [
    path('', views.invoice_list, name='invoice_list'),
    path('customer/add/', views.add_customer, name='add_customer'),
    path('customer/list/', views.list_customers, name='list_customers'),
    path('display/<int:invoice_id>/<int:style_id>/', views.display_invoice_style, name='display_invoice_style'),
    path('invoice/<int:invoice_id>/', views.invoice_detail, name='invoice_detail'),
    path('customer/<int:customer_id>/', views.customer_detail, name='customer_detail'),
    path('invoice/export_pdf/<int:invoice_id>/', views.invoice_export, name='invoice_export'),
    
    path('invoice/list/', views.InvoiceList.as_view()),
    path('invoice/create/', views.InvoiceCreateView.as_view(), name='invoice_form'),

    path('about/', views.about_view, name='about'),
]