import django_filters
from owner.models import Book
from django_filters import widgets
from django import forms


class BookFilter(django_filters.FilterSet):
    book_name=django_filters.CharFilter(lookup_expr="icontains",label="Book name",widget=widgets.forms.TextInput(attrs={"class":"form-control"}))
    author=django_filters.CharFilter(lookup_expr="icontains",label="Author",widget=widgets.forms.TextInput(attrs={"class":"form-control"}))
    price=django_filters.NumberFilter(widget=widgets.forms.TextInput(attrs={"class":"form-control"}))
    class Meta:
        model=Book
        fields=["book_name","author","price"]

