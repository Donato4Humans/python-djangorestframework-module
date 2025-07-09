# from django.db.models import QuerySet
# from django.http import QueryDict
#
# from rest_framework.exceptions import ValidationError
#
# from apps.pizza.models import PizzaModel
# from apps.pizza.serializers import PizzaSerializer
from random import choices

from django_filters import rest_framework as filters

from apps.pizza.models import DaysChoices

# def filter_pizza(query:QueryDict)->QuerySet:
#     qs = PizzaModel.objects.all()
#
#     for k, v in query.items():
#         match k:
#             case 'price_gt':
#                 qs = qs.filter(price__gt=v)
#             case 'price_lt':
#                 qs = qs.filter(price__lt=v)
#             case 'price_gte':
#                 qs = qs.filter(price__gte=v)
#             case 'price_lte':
#                 qs = qs.filter(price__lte=v)
#             case 'size_gt':
#                 qs = qs.filter(size__gt=v)
#             case 'size_lt':
#                 qs = qs.filter(size__lt=v)
#             case 'size_gte':
#                 qs = qs.filter(size__gte=v)
#             case 'size_lte':
#                 qs = qs.filter(size__lte=v)
#             case 'name_starts':
#                 qs = qs.filter(name__startswith=v)
#             case 'name_ends':
#                 qs = qs.filter(name__endswith=v)
#             case 'name_contains':
#                 qs = qs.filter(name__contains=v)
#             case 'order':
#                 fields = PizzaSerializer.Meta.fields
#                 allowed_fields = (*fields, *[f'-{field}' for field in fields])
#
#                 if v not in allowed_fields:
#                     raise ValidationError({'details':f'Only allowed : {allowed_fields}'})
#
#                 qs = qs.order_by(v)
#             case _:
#                 raise ValidationError({'details':f'{k} is not a valid filter'})
#
#     return qs



class PizzaFilter(filters.FilterSet): # most universal for filtering
    lt = filters.NumberFilter(field_name='price', lookup_expr='lt')
    range = filters.RangeFilter(field_name='size')# range_min=2&range_max=100
    price_in = filters.BaseInFilter(field_name='price')# price_in=30,25,2000
    day = filters.ChoiceFilter('day', choices=DaysChoices.choices)# for choice filtering
    order = filters.OrderingFilter(
        fields=(
            'id',
            'name',
            ('price','prc'), # if you need give other name for query param
        )
    ) # order=name asc
    # order=-name desc
