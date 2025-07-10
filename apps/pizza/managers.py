from django.db import models


# MANAGERS USED MOSTLY FOR FREQUENT DB REQUESTS
class PizzaQuerySet(models.QuerySet):
    def less_than_size(self, size):
        return self.filter(size__lt=size)

    def only_peperoni(self):
        return self.filter(name__startswith='Peperoni')


class PizzaManager(models.Manager):
    def get_queryset(self):
        return PizzaQuerySet(self.model)

    def less_than_size(self, size):
        return self.get_queryset().less_than_size(size)

    def only_peperoni(self):
        return self.get_queryset().only_peperoni()