from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from user.models import User
from user.serializers import UserSerializer


class ListCreateUserView(ListCreateAPIView):
    model = User
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Create a new User successful!'
            }, status=status.HTTP_201_CREATED)

        return JsonResponse({
            'message': 'Create a new User unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)


class UpdateDeleteUserView(RetrieveUpdateDestroyAPIView):
    model = User
    serializer_class = UserSerializer

    def get_queryset(self, *args, **kwargs):
        return User.objects.filter(id=self.kwargs['pk'])

    def put(self, request, *args, **kwargs):
        user = get_object_or_404(User, id=kwargs.get('pk'))
        snippet = User.objects.get(pk=user.id)
        serializer = UserSerializer(snippet, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Update User successful!'
            }, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Update User unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        user = get_object_or_404(User, id=kwargs.get('pk'))
        user.delete()

        return JsonResponse({
            'message': 'Delete User successful!'
        }, status=status.HTTP_200_OK)
