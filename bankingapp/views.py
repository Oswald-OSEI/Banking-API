from rest_framework.response import Response
from .models import BankAccount, Transaction
from random import randint 
from .serializers import BankAccountSerializer, TransactionSerializer
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view
# Create your views here.

def account_number_generator():
    const = "040"
    first_ = str(randint(100, 999))
    second_ = str(randint(100, 999))
    third_ = str(randint(1, 9))
    account_number = const + first_ + second_ + third_
    return account_number
@api_view(['POST'])
def create_bank_account(request):
    if request.method == "POST":
        account_details = BankAccountSerializer(data=request.data)
        if account_details.is_valid(raise_exception=True):
            j = account_number_generator()
            cd = account_details.data
            created_account = BankAccount.objects.create(
                user = request.user, 
                account_number = j, 
                balance = cd.get('balance')
            )
            created_account.save()
            return Response('Account Created Successfully')
@api_view(['GET'])
def view_bank_account(request):
    your_account = BankAccount.objects.get(user=request.user)
    account_data = BankAccountSerializer(your_account).data
    return Response(account_data)

@api_view(['GET','POST'])
def deposit(request):
    if request.method == "POST":
        your_transaction = TransactionSerializer(data=request.data)
        if your_transaction.is_valid(raise_exception=True):
            cd = your_transaction.data
            try:
                your_account = BankAccount.objects.get(user=request.user)
                if cd.get("bank_account_number")==your_account.account_number:
                    new_balance = your_account.balance + cd.get("amount")
                    your_account.balance = new_balance
                    your_account.save()
                    saved_transaction = Transaction.objects.create(
                        bank_account = your_account, 
                        bank_account_number = your_account.account_number,
                        amount = cd.get("amount"),
                        transaction_type = "deposit"
                    )
                    saved_transaction.save()
                    return Response("Transaction Successful")
                else:
                    return Response("wrong bank account")
            except ObjectDoesNotExist:
                return Response("you have no bank account")

@api_view(['GET','POST'])          
def withdrawal(request):
    if request.method == "POST":
        your_transaction = TransactionSerializer(data=request.data)
        if your_transaction.is_valid(raise_exception=True):
            cd = your_transaction.data
            try:
                your_account = BankAccount.objects.get(user=request.user)
                if cd.get("bank_account_number")==your_account.account_number:
                    if cd.get("amount") > your_account.balance:
                        return Response("You have less than the amount you want to withdraw")
                    else:
                        new_balance = your_account.balance - cd.get("amount")
                        your_account.balance = new_balance
                        your_account.save()
                    saved_transaction = Transaction.objects.create(
                        bank_account = your_account, 
                        bank_account_number = your_account.account_number,
                        amount = cd.get("amount"),
                        transaction_type = "withdrawal"
                    )
                    saved_transaction.save()
                    return Response("Transaction Successful")
                else:
                    return Response("wrong bank account")
            except ObjectDoesNotExist:
                return Response("you have no bank account")

@api_view(['GET'])            
def my_transactions(request):
    try:
        your_transactions = Transaction.objects.all().filter(bank_account__user=request.user)
        transactions_data = TransactionSerializer(your_transactions, many=True).data
        return Response(transactions_data)
    except ObjectDoesNotExist:
        return Response('you are not authorised to view history')








