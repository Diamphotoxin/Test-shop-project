from django import forms


class OrderForm(forms.Form):
    customer_name = forms.CharField(label='name', required=True)
    email = forms.EmailField(label='email', required=True)
    phone = forms.CharField(label='phone', required=True)

