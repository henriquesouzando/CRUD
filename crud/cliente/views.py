from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Cliente
from django.http import JsonResponse

class AjaxableResponseMixin:
   
    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
            }
            return JsonResponse(data)
        else:
            return response



class ClienteCreate(AjaxableResponseMixin,CreateView):
    model = Cliente
    fields = '__all__'

class ClienteUpdate(UpdateView):
    model = Cliente
    fields = '__all__'

class ClienteDelete(DeleteView):
    model = Cliente
  