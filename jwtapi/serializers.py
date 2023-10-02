from rest_framework import serializers
from django.contrib.auth.models import User
from . models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterUser
        fields = ['id','username','email','city','mobileNo','password']


    def save(self, **kwargs):
        user = RegisterUser.objects.create_user(username = self.validated_data['username'], email=self.validated_data['email'],city = self.validated_data['city'],
                    mobileNo = self.validated_data['mobileNo'], password=self.validated_data['password']  
                    )

        user.save()
        return user
    


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        
        
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"