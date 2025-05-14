from django import forms
from .models import *

class ShoppingForm(forms.ModelForm):
    shopping_full_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام کامل'}),
        required=True,
        max_length=30,
        label='',
    )
    shopping_email = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل'}),
        required=True,
        max_length=60,
        label='',
    )
    shopping_address1 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'آدرس اول'}),
                               required=True,
                               max_length=110,
                                        label='',)
    shopping_address2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'آدرس دوم'}),
                               required=False,
                               max_length=110,
                                        label='',)
    shopping_city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'شهر'}),
                           required=True,
                           max_length=30,
                                    label='',)
    shopping_state = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'منطقه'}),
                            required=True,
                            max_length=30,
                                     label='',)
    shopping_zipcode = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'کد پستی'}),
                              required=True,
                              max_length=30,
                                       label='',)
    shopping_country = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'کشور'}),
                              required=False,
                              max_length=25,
                                       label='',)

    class Meta:
        model = ShoppingAddress
        fields = ('shopping_full_name', 'shopping_email','shopping_address1','shopping_address2','shopping_city',
                  'shopping_state','shopping_zipcode','shopping_country')
        exclude = ('user',)



