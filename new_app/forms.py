from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from new_app import models
from new_app.models import Login, seller, customer, product


class login_form(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label="password",widget=forms.PasswordInput)
    password2 = forms.CharField(label="confirm password",widget=forms.PasswordInput)
    class Meta:
        model = Login
        fields = "username","password1","password2"


class seller_form(forms.ModelForm):

    class Meta:

        model = seller
        fields = "name","email","gst_no","product_category"


class customer_form(forms.ModelForm):

    class Meta:

        model = customer
        fields = "name","email","address","phone_no"


class product_form(forms.ModelForm):
     class Meta:
         model = product
         fields = "__all__"
         exclude = ('product_user',)

