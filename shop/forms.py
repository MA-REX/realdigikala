from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm
from django import forms
from .models import Profile


class UpdateUserInfo(forms.ModelForm):

    phone = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'شماره همراه'}),
        required=False,
        max_length=11,
    )
    address1 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'آدرس اول'}),
        required=False,
        max_length=110,)
    address2 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'آدرس دوم'}),
        required=False,
        max_length=110,)
    city = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'شهر'}),
        required=False,
        max_length=30,)
    state = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'منطقه'}),
        required=False,
        max_length=30,)
    zipcode = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'کد پستی'}),
        required=False,
        max_length=30,)
    country = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'کشور'}),
        required=False,
        max_length=25,)

    class Meta:
        model = Profile
        fields = ('phone', 'address1','address2','city','state','zipcode','country')


class UpdateUserForm(UserChangeForm):
    password = None
    first_name = forms.CharField(
        label='', max_length=25, widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'نام خود را وارد کنید'})
    )
    last_name = forms.CharField(
        label='', max_length=25, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام خانوادگی خود را وارد کنید'})
    )
    email = forms.EmailField(
        label='',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل را وارد کنید '})
    )
    username = forms.CharField(
        label='', widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'نام کاربری'})
    )


    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        label='', max_length=25, widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'نام خود را وارد کنید'})
    )
    last_name = forms.CharField(
        label='', max_length=25, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام خانوادگی خود را وارد کنید'})
    )
    email = forms.EmailField(
        label='',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل را وارد کنید '})
    )
    username = forms.CharField(
        label='', widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'نام کاربری'})
    )
    password1 = forms.CharField(
        label='', widget=forms.PasswordInput(
            attrs={'class' : 'form-control',
                                                    'name': 'password',
                                                    'type': 'password',
                                                    'placeholder': 'رمزتو بزن'})
    )
    password2 = forms.CharField(
        label='', widget=forms.PasswordInput(
            attrs={'class': 'form-control',
                                                    'name': 'password',
                                                    'type': 'password',
                                                    'placeholder': 'دوباره رمزتو بزن'})
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')


class UpdatePasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label='', widget=forms.PasswordInput(
            attrs={'class' : 'form-control',
                                                    'name': 'password',
                                                    'type': 'password',
                                                    'placeholder': 'رمزتو بزن'})
    )
    new_password2 = forms.CharField(
        label='', widget=forms.PasswordInput(
            attrs={'class': 'form-control',
                                                    'name': 'password',
                                                    'type': 'password',
                                                    'placeholder': 'دوباره رمزتو بزن'})
    )

    class Meta:
        model = User
        fields = ('new_password1', 'new_password2')



