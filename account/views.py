from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.request import Request
from django.http import HttpRequest
from .models import Account, loginmodel
from django.contrib.auth import authenticate, login
from .serializers import AccountSerializer, loginSerializer
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['POST'])
def registration(request):
    if request.method == "POST":
        reg_request = AccountSerializer(data = request.data)
        if reg_request.is_valid(raise_exception=True):
            cd = reg_request.validated_data
            registering = Account.objects.create(
                email = cd.get("email"), 
                first_name = cd.get('first_name'), 
                last_name = cd.get("last_name"), 
                telephone_number = cd.get("telephone_number"), 
                Gender = cd.get("Gender"), 
                date_of_birth = cd.get("date_of_birth"), 
                passport_picture = request.FILES.get("pasport_picture"),
                Id_type = cd.get("Id_type"), 
                Id_number = cd.get("Id_number")
            )
            registering.set_password(cd.get("password"))
            registering.save()
            return Response("Registration Successful")
        
@api_view(['POST'])
def user_login(request):
    userlogins = loginSerializer(data=request.data)
    if userlogins.is_valid(raise_exception = True):
        cd = userlogins.validated_data
        authorize = authenticate(request, username=cd.get('email'), password=cd.get('password'))
        if authorize is not None:
            if authorize.is_active:
                login(request, authorize)
                return Response("login succesful")
            else:
                return Response("your account is blocked. Contact Customer Care")
        else:
            return Response("account does not exist")
                
