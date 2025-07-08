#from django.db.models import Q
#from django.db.models.aggregates import Min, Max, Count
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request

from apps.pizza.filter import filter_pizza
from apps.pizza.models import PizzaModel
from apps.pizza.serializers import PizzaSerializer

from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin

# class PizzaListCreateView(APIView):
#     def get(self, request:Request, *args, **kwargs):
#         #pizzas = PizzaModel.objects.all() # just creates query_set but no DB request(request will be sent when it needed for some actions)
#         #pizzas = pizzas.filter(size__gt=5, name='Peperoni') # if you need filter several conditions(AND)
#         #pizzas = pizzas.filter(Q(size__gt=50) | Q(name='Peperoni' & Q())) # if you need filter several conditions(OR)
#
#         #pizzas = PizzaModel.objects.filter(Q(size__gt=50) | Q(name='Peperoni')).exclude(price=5656).order_by('price', '-size').reverse()
#         #pizzas = PizzaModel.objects.all()[0:3]# [0:6:2] when we add step, python takes query result and makes DB request instantly
#         #pizzas = PizzaModel.objects.all().values('id', 'name', 'price') # when you need check specific fields(serializer must be changed)
#         #pizzas = PizzaModel.objects.aggregate(Min('size'), Max('size'))
#         #pizzas = PizzaModel.objects.values('name').annotate(count=Count('name')) # count how many items of specific field with same values
#         #query_set = PizzaModel.objects.all()
#         query_set = filter_pizza(request.query_params) # for custom filter func
#         serializer = PizzaSerializer(query_set, many=True)
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def post(self, *args, **kwargs):
#         data = self.request.data
#         serializer = PizzaSerializer(data=data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_201_CREATED)
#
# class PizzaRetrieveUpdateDestroyView(APIView):
#     def get(self, *args, **kwargs):
#         pk = kwargs['pk']
#
#         try:
#             pizza = PizzaModel.objects.get(pk=pk)
#         except PizzaModel.DoesNotExist:
#             return Response({'details':'Not found'}, status.HTTP_404_NOT_FOUND)
#
#         serializer = PizzaSerializer(pizza)
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def put(self, *args, **kwargs):
#         pk = kwargs['pk']
#
#         try:
#             pizza = PizzaModel.objects.get(pk=pk)
#         except PizzaModel.DoesNotExist:
#             return Response({'details':'Not found'}, status.HTTP_404_NOT_FOUND)
#
#         data = self.request.data
#         serializer = PizzaSerializer(pizza, data=data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def delete(self, *args, **kwargs):
#         pk = kwargs['pk']
#
#         try:
#             PizzaModel.objects.get(pk=pk).delete()
#         except PizzaModel.DoesNotExist:
#             return Response({'details':'Not found'}, status.HTTP_404_NOT_FOUND)
#
#         return Response({'details':'Deleted!'}, status.HTTP_204_NO_CONTENT)

# class PizzaListCreateView(GenericAPIView, ListModelMixin, CreateModelMixin): # no changes for this view with new GenericAPIView parent class
#     #queryset = PizzaModel.objects.all()
#     serializer_class = PizzaSerializer
#
#     def get_queryset(self): # if you need custom filter
#         request:Request = self.request
#         return filter_pizza(request.query_params)
#
#     def get(self, request, *args, **kwargs):
#         return super().list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return super().create(request, *args, **kwargs)

    # def get(self, request: Request, *args, **kwargs):
    #     query_set = filter_pizza(request.query_params)
    #     serializer = PizzaSerializer(query_set, many=True)
    #     return Response(serializer.data, status.HTTP_200_OK)
    #
    # def post(self, *args, **kwargs):
    #     data = self.request.data
    #     serializer = PizzaSerializer(data=data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status.HTTP_201_CREATED)

# class PizzaRetrieveUpdateDestroyView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin): # here we can simplify some actions
#     serializer_class = PizzaSerializer
#     queryset = PizzaModel.objects.all()
#
#     def get(self, request, *args, **kwargs):
#         return super().retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return super().update(request, *args, **kwargs)
#
#     def patch(self, request, *args, **kwargs): # for partial_update of DB
#         return super().partial_update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return super().destroy(request, *args, **kwargs)

    # def get(self, *args, **kwargs):
    #     pizza = self.get_object()
    #     # pk = kwargs['pk']
    #     #
    #     # try:
    #     #     pizza = PizzaModel.objects.get(pk=pk)
    #     # except PizzaModel.DoesNotExist:
    #     #     return Response({'details':'Not found'}, status.HTTP_404_NOT_FOUND)
    #
    #     serializer = PizzaSerializer(pizza)
    #     return Response(serializer.data, status.HTTP_200_OK)

    # def put(self, *args, **kwargs):
    #     pizza = self.get_object()
    #     # pk = kwargs['pk']
    #     #
    #     # try:
    #     #     pizza = PizzaModel.objects.get(pk=pk)
    #     # except PizzaModel.DoesNotExist:
    #     #     return Response({'details':'Not found'}, status.HTTP_404_NOT_FOUND)
    #
    #     data = self.request.data
    #     serializer = PizzaSerializer(pizza, data=data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status.HTTP_200_OK)

    # def delete(self, *args, **kwargs):
    #     # pk = kwargs['pk']
    #     #
    #     # try:
    #     #     PizzaModel.objects.get(pk=pk).delete()
    #     # except PizzaModel.DoesNotExist:
    #     #     return Response({'details':'Not found'}, status.HTTP_404_NOT_FOUND)
    #     self.get_object().delete()
    #
    #     return Response({'details':'Deleted!'}, status.HTTP_204_NO_CONTENT)


class PizzaListCreateView(ListCreateAPIView): # even more simple with parent class
    #queryset = PizzaModel.objects.all() # we have it inside custom filter
    serializer_class = PizzaSerializer

    def get_queryset(self): # if you need custom filter
        request:Request = self.request
        return filter_pizza(request.query_params)


class PizzaRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = PizzaSerializer
    queryset = PizzaModel.objects.all()
    http_method_names = ['get', 'put', 'delete'] # we can forbid not needed http-methods