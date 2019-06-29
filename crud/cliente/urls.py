from django.urls import path
from .views import  ClienteCreate


urlpatterns = [
    path('novo', ClienteCreate.as_view(), name='cadastrar_cliente'),
 
]