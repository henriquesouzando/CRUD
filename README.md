# CRUD
CRUD simple com python e django.  
Eu utilzei o conceito class based views do django pois ele permite estruturar as viewe e reutilizar código aproveitando heranças e mixins. 

# Tratamento de envio de mensagens
```
class FormMessageMixin(object):
    @property
    def form_valid_message(self):
        return NotImplemented

    form_invalid_message = 'Please correct the errors below.'

    def form_valid(self, form):
        messages.success(self.request, self.form_valid_message)
        return super(FormMessageMixin, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, self.form_invalid_message)
        return super(FormMessageMixin, self).form_invalid(form)
```
Eu criei a class FormMessageMixin para reaproveitar as funções de tratamento de sucesso ou falha para apresentar no front e informar os usuários se sua ação foi executada com sucesso ou não. 

# List view
```
class ClienteView(ListView):
    model = Cliente
    context_object_name = 'clientes'
    paginate_by = 1
    
    def get_context_data(self, **kwargs):
        context = super(ClienteView, self).get_context_data(**kwargs)
        clientes = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(clientes, self.paginate_by)
        try:
            clientes = paginator.page(page)
        except PageNotAnInteger:
            clientes = paginator.page(1)
        except EmptyPage:
            clientes = paginator.page(paginator.num_pages)
        context['clientes'] = clientes
        return context
```

Criei a classe ClienteView herdando o módulo ListView que criará uma nova chamada de exibição. Logo em seguida eu criei a função get_context_data para tratar a nossa paginação. 

# URL
```
from django.urls import path
from .views import  ClienteCreate, ClienteView, ClienteUpdate, ClienteRemover


urlpatterns = [
    path('novo', ClienteCreate.as_view(), name='cadastrar_cliente'),
    path('update/<int:pk>/', ClienteUpdate.as_view(), name='cliente_editar'),
    path('', ClienteView.as_view(), name='listar_cliente'),
    path('remover/<int:pk>/', ClienteRemover.as_view(), name='cliente_remover')
 
]
```
Criei o a url para a nossa classe ClienteView. 

