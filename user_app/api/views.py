from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializer import RegistrationSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from user_app import models
from rest_framework.authtoken.models import Token

@api_view(['POST'])
def registrationView(request):
    if request.method=='POST':
        serializer=RegistrationSerializer(data=request.data)
        dataa={}
        if serializer.is_valid():
            account=serializer.save()
            dataa['user']=account.username
            dataa['email']=account.email
            dataa['token']=Token.objects.get(data=account).key
        else:
            dataa=serializer.errors
            
        return Response(dataa)


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
        