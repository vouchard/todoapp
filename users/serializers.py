from wsgiref.validate import validator
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator

class UserRegSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True,validators=[UniqueValidator(queryset=User.objects.all())])
    username = serializers.CharField(required = True,validators=[UniqueValidator(queryset=User.objects.all())])
    first_name = serializers.CharField(required = True)
    last_name = serializers.CharField(required = True)
    password = serializers.CharField(required = True)
    class Meta:
        model = User
        fields = ['username','password','first_name','last_name','email']

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True,validators=[UniqueValidator(queryset=User.objects.all())])
    username = serializers.CharField(required = True,validators=[UniqueValidator(queryset=User.objects.all())])
    first_name = serializers.CharField(required = True)
    last_name = serializers.CharField(required = True)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
 