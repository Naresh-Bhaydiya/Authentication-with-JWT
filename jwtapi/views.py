from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *

from rest_framework import status
from django.contrib.auth import authenticate,logout
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken



def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class signupAPI(APIView):
    """docstring for signupAPI."""
    def post(self,request):
        serializer = UserSerializer(data= request.data)
        if serializer.is_valid(raise_exception=True):
            user =  serializer.save()          
            token = get_tokens_for_user(user=user)
            serializer = UserSerializer(user)
            data = {
                'user':serializer.data,
                'token':token
            }
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



class loginAPI(APIView):
    def post(self, request):
        data = request.data
        authenticate_user = authenticate(username=data['username'], password=data['password'])
        if authenticate_user is not None:
            user = User.objects.get(username=data['username'])
            serializer = LoginSerializer(user)
            token = get_tokens_for_user(user=user)
            response_data = {
                "user": serializer.data,
                "token": token
            }
            if token:
                response_data['token'] = token
            return Response({"status": status.HTTP_200_OK, "Data": response_data})
        return Response({"message": "details not found !"}, status=status.HTTP_404_NOT_FOUND)


class BookAPI(APIView):
    authentication_classes = [JWTAuthentication,SessionAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self,request):
        data = request.data
        serializer = BookSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()        
            response_data = {
                "messege":"Books Created Successfully !",
                "user":serializer.data
            }            
            return Response({"status":status.HTTP_200_OK,"Data":response_data})
        return Response({"message":"details not found !"},status=status.HTTP_404_NOT_FOUND)
    
    def get(self,request):
        books = Book.objects.all().order_by('-id')[:5]
        serializer = BookSerializer(books,many=True)
        return Response({"status":status.HTTP_200_OK,"Data":serializer.data})
