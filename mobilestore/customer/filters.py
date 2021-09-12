import django_filters
from django_filters import CharFilter
from owner.models import Mobile
from django import forms
from django_filters import widgets
class MobileFilter(django_filters.FilterSet):
    mobile_name = django_filters.CharFilter(lookup_expr="icontains",label="Mobile name",widget=widgets.forms.TextInput(attrs={"class":"form-control"}))
    brand_name = django_filters.CharFilter(lookup_expr="icontains",label="Brand Name",widget=widgets.forms.TextInput(attrs={"class":"form-control"}))
    price=django_filters.NumberFilter(widget=widgets.forms.TextInput(attrs={"class":"form-control"}))
    class Meta:
        model=Mobile

        fields=["mobile_name","brand_name","price"]




