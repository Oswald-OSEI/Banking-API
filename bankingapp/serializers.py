from rest_framework import serializers
from .models import BankAccount, Transaction

class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = ['account_number','balance', 'Date_created']

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['bank_account_number','amount', 'transaction_date', 'transaction_type']