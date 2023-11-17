from django import forms
from django.forms import inlineformset_factory
from django.forms.models import BaseInlineFormSet
from .models import Customer, Invoice, InvoiceItem


class CustomerCreateForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'address', 'legal_number',
                  'postal_code', 'city', 'email', 'phone',
                  'website', 'description']
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['name'].widget.attrs.update({'class': 'form-control'})
            self.fields['legal_number'].widget.attrs.update({'class': 'text-white'})



class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        # We set the user field automatically in the view.
        fields = ('title', 
                    'customer', 'issuer_legal_number',
                    'concept', 'slug', 'issue_date',
                    'iban', 'irpf')
        

class InvoiceItemForm(forms.ModelForm):
    class Meta:
        model = InvoiceItem
        fields = '__all__'


InvoiceItemInlineFormset = inlineformset_factory(
    Invoice,
    InvoiceItem,
    form=InvoiceItemForm,
    extra=5,
)