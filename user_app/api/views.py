from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializer import RegistrationSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from user_app import models
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import AuthenticationFailed


@api_view(['POST'])
def logout_view(request):
    if request.method=='POST':
        request.user.auth_token.delete()
        return Response(status=200)

@api_view(['POST'])
def registrationView(request):
    if request.method=='POST':
        serializer=RegistrationSerializer(data=request.data)
        data={}
        if serializer.is_valid():
            account=serializer.save()
            data['user']=account.username
            data['email']=account.email
            #data['token']=Token.objects.get(user=account).key
            refresh=RefreshToken.for_user(account)
            data['token']={
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }

        else:
            data=serializer.errors
            
        return Response(data,status=201)


# class registrationView(APIView):
#     def post(self,request):
#         serializer=RegistrationSerializer(data=request.data)
#         dataa={}
#         if serializer.is_valid():
#             account=serializer.save()
#             dataa['user']=account.username
#             dataa['email']=account.email
#             dataa['token']=Token.objects.get(data=account).key
#         else:
#             dataa=serializer.errors
            
#         return Response(dataa)
        