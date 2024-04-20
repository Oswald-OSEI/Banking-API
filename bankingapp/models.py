from django.db import models
from account.models import Account
# Create your models here.

class BankAccount(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, null = True)
    account_number = models.CharField(max_length=10, unique=True, null = True)
    balance = models.IntegerField()
    Date_created = models.DateField(auto_now=True)

class Transaction(models.Model):
    bank_account = models.ForeignKey(BankAccount, on_delete=models.CASCADE, null = True)
    bank_account_number = models.CharField(max_length=10)
    amount = models.IntegerField()
    transaction_date = models.DateField(auto_now=True)
    