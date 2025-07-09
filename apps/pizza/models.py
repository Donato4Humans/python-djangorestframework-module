from django.core import validators as V
from django.core.validators import MinValueValidator
from django.db import models

from core.enums.regex_enum import RegexEnum
from core.models import BaseModel

from apps.pizza_shop.models import PizzaShopModel


class DaysChoices(models.TextChoices): # another way to validate further with choices
    MONDAY = 'Monday'
    TUESDAY = 'Tuesday'
    WEDNESDAY = 'Wednesday'
    THURSDAY = 'Thursday'
    FRIDAY = 'Friday'
    SATURDAY = 'Saturday'
    SUNDAY = 'Sunday'

class PizzaModel(BaseModel):
    class Meta:
        db_table = 'pizzas'
        #ordering = ('id',) # if you need change default ordering in DB

    # name = models.CharField(max_length=50, blank=True) # default model validation, blank allows to not fill name field
    # size = models.IntegerField(default=22) # sets default value if not specified
    # price = models.FloatField(null=True) # not proper way to use null, it is only advised to use with foreign keys when it`s deleted but you need save data
    # pizza_shop = models.ForeignKey(PizzaShopModel, on_delete=models.CASCADE, related_name='pizzas')
    name = models.CharField(max_length=20, validators=[V.RegexValidator(RegexEnum.NAME.pattern, RegexEnum.NAME.msg)]) # custom validator enum
    size = models.IntegerField(validators=[V.MinValueValidator(1), V.MaxValueValidator(100)]) # ready val. from lib
    price = models.FloatField()
    day = models.CharField(max_length=9, choices=DaysChoices.choices) # as choices can be set only const entities like(days, months, etc.)
    pizza_shop = models.ForeignKey(PizzaShopModel, on_delete=models.CASCADE, related_name='pizzas')