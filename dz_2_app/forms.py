from django import forms


class ProductImageForm(forms.Form):
    product_image = forms.ImageField()

