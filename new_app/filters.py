import django_filters
from django import forms
from django_filters import CharFilter

from new_app.models import product


class BrandFilter(django_filters.FilterSet):
    brand = CharFilter(label="", lookup_expr='icontains', widget=forms.TextInput(attrs={'placeholder': 'Search brand','class':'form-control'}))

    class Meta:
        model = product
        fields = ('brand',)

class SellerFilter(django_filters.FilterSet):
    product_user__name = CharFilter(label="", lookup_expr='icontains', widget=forms.TextInput(attrs={'placeholder': 'Search seller','class':'form-control'}))
    class Meta:
        model = product
        fields = ('product_user__name',)


