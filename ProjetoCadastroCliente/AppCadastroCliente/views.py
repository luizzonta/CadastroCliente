from django.views.generic import TemplateView
from django.views.generic import ListView
from ProjetoCadastroCliente.models import Cliente
from django.views.generic import CreateView
from django.urls.base import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView


class Index(TemplateView):
    template_name = "index.html"
    
class ListaCliente(ListView):
    template_name = "lista.html"
    model = Cliente
    context_object_name = 'cliente'

class CriaCliente(CreateView): 
    template_name = "cadastro.html"
    model = Cliente()
    fields = '__all__'
    success_url = reverse_lazy("lista_cliente")

class AtualizaCliente(UpdateView):
    template_name = "atualiza.html"
    model = Cliente()
    fields = '__all__'
    context_object_name = 'cliente'
    success_url = reverse_lazy("lista_cliente")

class DeletaCliente(DeleteView):
    template_name = "exclui.html"
    model = Cliente()
    context_object_name = 'cliente'
    success_url = reverse_lazy("lista_cliente")