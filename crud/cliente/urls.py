from django.urls import path
from .views import  ClienteCreate, ClienteView, ClienteUpdate, ClienteRemover


urlpatterns = [
    path('novo', ClienteCreate.as_view(), name='cadastrar_cliente'),
    path('update/<int:pk>/', ClienteUpdate.as_view(), name='cliente_editar'),
    path('', ClienteView.as_view(), name='listar_cliente'),
    path('remover/<int:pk>/', ClienteRemover.as_view(), name='cliente_remover')
 
]