from django.contrib import admin
from .models import Account
from bankingapp.models import BankAccount, Transaction
from django.contrib.auth.admin import UserAdmin


# Register your models here.
class UserAccount(UserAdmin):
    list_display = ('email','first_name',  'last_name',  'last_login', 'is_active',)
    ordering = ['email']
    filter_horizontal = ()
    list_filter = ()
# makes password field readonly
    fieldsets = ()    
admin.site.register(Account, UserAccount)

class BankAccountAdmin(admin.ModelAdmin):
    model = BankAccount
    list_display = ('user', 'account_number','balance','Date_created')
    ordering = ('user',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
admin.site.register(BankAccount, BankAccountAdmin)

class TransactionAdmin(admin.ModelAdmin):
    model = Transaction
    list_display = ('bank_account', 'bank_account_number','amount','transaction_date')
    ordering = ('transaction_date',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
admin.site.register(Transaction, TransactionAdmin)

