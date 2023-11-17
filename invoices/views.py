from typing import Any
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.db import transaction
from django.views.generic import CreateView, ListView
from django.forms import modelformset_factory
from django.contrib.auth.mixins import LoginRequiredMixin
import weasyprint

from .forms import CustomerCreateForm, InvoiceForm, InvoiceItemInlineFormset
from .models import Invoice, Customer, InvoiceStyles



@login_required
def invoice_list(request):
    invoices = Invoice.objects.filter(user=request.user.id)
    return render(request, 'invoices/invoice/list.html', {'invoices': invoices})


@login_required
def invoice_detail(request, invoice_id):
    invoice = get_object_or_404(Invoice, id=invoice_id)
    
    return render(request, 'invoices/invoice/detail.html', {'invoice': invoice})


@login_required
def invoice_export(request, invoice_id):
    invoice = get_object_or_404(Invoice, id=invoice_id)
    html = render_to_string(f'invoices/invoice/invoice_styles/{invoice.style}.html', {'invoice': invoice})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename=invoice_{invoice.id}.pdf'
    weasyprint.HTML(string=html, base_url=request.build_absolute_uri()).write_pdf(response)
    return response



@login_required
def add_customer(request):
    if request.method == 'POST':
        form = CustomerCreateForm(request.POST)
        if form.is_valid():
            customer = form.save()
            return redirect(reverse('invoices:list_customers'))
    else:
        form = CustomerCreateForm()

    return render(request, 'invoices/customer/add.html',
                  {'form': form})

@login_required
def display_invoice_style(request, invoice_id, style_id):
    '''Displays the selected invoice style for the invoice'''
    return render(request, 'invoices/invoice/invoice_styles/style_01.html')


@login_required
def list_customers(request):
    customers = Customer.objects.all()
    return render(request, 'invoices/customer/list.html',
                  {'customers': customers})


@login_required
def customer_detail(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    return render(request, 'invoices/customer/detail.html', {'customer': customer})




class InvoiceList(LoginRequiredMixin, ListView):
    model = Invoice

class InvoiceCreateView(LoginRequiredMixin, CreateView):
    login_required = True
    form_class = InvoiceForm
    template_name = 'invoices/invoice_form.html'

    def get_context_data(self, **kwargs):
        context = super(InvoiceCreateView, self).get_context_data(**kwargs)
        context['invoice_item_formset'] = InvoiceItemInlineFormset()
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        invoice_item_formset = InvoiceItemInlineFormset(self.request.POST)

        if form.is_valid() and invoice_item_formset.is_valid():
            return self.form_valid(form, invoice_item_formset)
        else:
            return self.form_invalid(form, invoice_item_formset)
        
    def form_valid(self, form, invoice_item_formset):
        self.object = form.save(commit=False)
        self.object.user_id = self.request.user.id
        self.object.save()
        # save invoice item instances
        invoice_items = invoice_item_formset.save(commit=False)
        for item in invoice_items:
            item.invoice = self.object 
            item.save()
        return redirect(reverse('invoices:invoice_list'))
    
    def form_invalid(self, form, invoice_item_formset):
        print("\n\nError\n\n")
        return self.render_to_response(
            self.get_context_data(form=form,
                                  invoice_item_formset=invoice_item_formset)
        )
    

def about_view(request):
    return render(request, 'about.html')