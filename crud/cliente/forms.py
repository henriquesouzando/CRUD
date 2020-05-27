from .models import Cliente
from bootstrap_modal_forms.forms import BSModalForm
from django import forms

class ClientesForm(BSModalForm,forms.ModelForm ):
   class Meta:
        model = Cliente
        fields = '__all__'
        