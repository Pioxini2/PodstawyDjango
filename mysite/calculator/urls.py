from django.urls import path
from .views import calc, hello

urlpatterns = [
    path('hello/<int:number>', hello),
    path('calc', calc)
]