from rest_framework.response import Response
from rest_framework.views import APIView
from django.forms import model_to_dict
from rest_framework import status

from users.models import UserModel
from users.serializers import UserSerializer


class UserListCreateView(APIView):
    def get(self, *args, **kwargs):
        users = UserModel.objects.all()
        serializer = UserSerializer(instance=users, many=True) # instance can get only data that is saved into DB
        # response = [model_to_dict(user) for user in users] # not proper way
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data
        # user = UserModel(name=data['name'], age=data['age'], status=data['status'], weight=data['weight'])
        # user.save()
        # response = {'name': user.name, 'age': user.age, 'status': user.status, 'weight': user.weight} not best way
        serializer =  UserSerializer(data=data)

        # if not serializer.is_valid():
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.is_valid(raise_exception=True) # same as above if statement and return
        serializer.save()
        # user = UserModel.objects.create(**serializer.data) # second way to create and save to DB like in above lines
        # response = model_to_dict(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class UserRetrieveUpdateDestroyView(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs["pk"]

        try:
            user = UserModel.objects.get(pk=pk)
        except UserModel.DoesNotExist:
            return Response(f"User {pk} doesn't exist")
        serializer = UserSerializer(user)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        pk = kwargs["pk"]

        try:
            user = UserModel.objects.get(pk=pk)
        except UserModel.DoesNotExist:
            return Response(f"User {pk} doesn't exist")

        data = self.request.data
        serializer = UserSerializer(instance=user, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # for k, v in data.items(): way to update without serializer
        #     setattr(user, k, v)
        # user.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, *args, **kwargs): # no need in serializers for delete
        pk = kwargs["pk"]

        try:
            UserModel.objects.get(pk=pk).delete()
        except UserModel.DoesNotExist:
            return Response(f"User {pk} doesn't exist")

        return Response(status=status.HTTP_204_NO_CONTENT)

