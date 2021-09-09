import django_filters
from owner.models import Mobile

class MobileFilter(django_filters.FilterSet):
    mobile_name=django_filters.CharFilter(lookup_expr="icontains")
    brand_name=django_filters.CharFilter(lookup_expr="icontains")
    class Meta:
        model=Mobile
        fields=["price"]
