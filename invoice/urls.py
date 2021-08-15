from django.urls import path
from . import views

urlpatterns = [
path('login',views.login, name='login'),
path('logout',views.logout, name='logout'),
path('dashboard',views.dashboard, name='dashboard'),
path('invoices',views.invoices, name='invoices'),
path('products',views.products, name='products'),
path('clients',views.clients, name='clients'),
]
