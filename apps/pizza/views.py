from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.request import Request

from apps.pizza.filter import PizzaFilter
from apps.pizza.models import PizzaModel
from apps.pizza.serializers import PizzaSerializer


class PizzaListCreateView(ListAPIView):
    serializer_class = PizzaSerializer
    queryset = PizzaModel.objects.all()
    filterset_class = PizzaFilter
    #pagination_class = None # if you don`t need pagination for specific view(rare case, by default pagination MUST BE IMPLEMENTED)

    # def get_queryset(self):
    #     request:Request = self.request
    #     return filter_pizza(request.query_params)


class PizzaRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = PizzaSerializer
    queryset = PizzaModel.objects.all()
    http_method_names = ['get', 'put', 'patch', 'delete']