from django.urls import path
from .views import add_user, calc, get_users, hello

urlpatterns = [
    path('hello/<int:number>', hello),
    path('calc', calc),
    path('users', get_users),
    path('add_user', add_user)
]