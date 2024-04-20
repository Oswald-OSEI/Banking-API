from django.urls import path
from .import views

urlpatterns=[
path('create account/', views.create_bank_account),
path('withdraw/', views.withdrawal), 
path('deposit/' , views.deposit),
path('view my account/', views.view_bank_account),
path('my transactions/', views.my_transactions),
]