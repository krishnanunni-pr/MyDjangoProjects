import django_filters
from reporting.models import TimeSheet,MyUser,Batch
from django import forms



class TimeSheetFilter(django_filters.FilterSet):
    user=django_filters.ModelChoiceFilter(queryset=MyUser.objects.all(),
                                          widget=forms.Select(attrs={'class':'form-select'}))
    batch = django_filters.ModelChoiceFilter(queryset=Batch.objects.all(),
                                            widget=forms.Select(attrs={'class': 'form-select'}))

    date=django_filters.DateFilter(widget=forms.DateInput(attrs={'class':'date'}))


    class Meta:
        model=TimeSheet
        fields=['date','batch','user']