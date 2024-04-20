from rest_framework import serializers
from .models import Account, loginmodel

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['email', 'first_name', 'last_name', 'telephone_number', 'passport_picture', 'Gender', 'date_of_birth', 'Id_type', "Id_number",'password']
        write_only_fields = ['password']

class loginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={"input_type": "password"})
    class Meta:
        model = loginmodel
        fields = ['email', 'password']
        write_only_fields = ["password"]