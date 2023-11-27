from django.urls import path
from .views import calc, get_users, hello

urlpatterns = [
    path('hello/<int:number>', hello),
    path('calc', calc),
    path('users', get_users)
]