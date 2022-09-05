from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import status, viewsets
from users.serializers import UserRegSerializer,UserSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    serializer_class =  UserSerializer
    queryset = User.objects.all()
    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [AllowAny]
        return super().get_permissions()

    def create(self, request, *args, **kwargs):
        self.serializer_class = UserRegSerializer
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            usr = User.objects.create(
                username = serializer.validated_data.get('username'),
                email = serializer.validated_data.get('email'),
                first_name = serializer.validated_data.get('first_name'),
                last_name = serializer.validated_data.get('last_name')
            )
            usr.set_password(serializer.validated_data.get('password'))
            usr.save()
            serializer.validated_data.pop('password')
        else:
            return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
        return Response(serializer.validated_data,status = status.HTTP_201_CREATED)