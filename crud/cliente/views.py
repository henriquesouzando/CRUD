from django.urls import reverse_lazy
from django.contrib import messages

from django.views.generic.list import ListView

from .models import Cliente
from .forms import ClientesForm

from django.http import JsonResponse

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView, BSModalDeleteView, BSModalReadView



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

class ClienteCreate(FormMessageMixin,BSModalCreateView):
    model = Cliente
    template_name = 'cliente/cliente_form.html'
    form_class = ClientesForm
    success_url = reverse_lazy('listar_cliente')
    form_valid_message = 'Cliente cadastrado com sucesso!'

class ClienteUpdate(FormMessageMixin, BSModalUpdateView):
    model = Cliente
    template_name = 'cliente/cliente_form.html'
    form_class = ClientesForm
    success_url = reverse_lazy('listar_cliente')
    form_valid_message = 'Produto atualizado com sucesso!'

class ClienteRemover(FormMessageMixin, BSModalDeleteView):
    model = Cliente
    template_name = 'cliente/cliente_remover.html'
    success_message = 'cliente deletado com sucesso!!.'
    success_url = reverse_lazy('listar_cliente')
    
  