import django_filters
from .models import Garment

class GarmentFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains', label='Name')
    brand = django_filters.CharFilter(lookup_expr='icontains', label='Brand')
    type = django_filters.ChoiceFilter(choices=Garment.Type.choices, label='Type')
    thrifted = django_filters.BooleanFilter(label='Thrifted')

    class Meta:
        model = Garment
        fields = ['type', 'brand', 'name', 'thrifted']