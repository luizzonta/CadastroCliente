from django.urls import path
from AppCadastroCliente.views import Index, ListaCliente, CriaCliente,\
    AtualizaCliente, DeletaCliente
from ProjetoCadastroCliente.models import Cliente


urlpatterns = [
    path('',Index.as_view(), name="index"),
    path('cliente/',ListaCliente.as_view(),name='lista_cliente'),
    path('cliente/cadastrar', CriaCliente.as_view(model=Cliente), name="cadastra_cliente"),
    path('cliente/<pk>', AtualizaCliente.as_view(model=Cliente), name="atualiza_cliente"),
    path('cliente/excluir/<pk>', DeletaCliente.as_view(model=Cliente), name="deleta_cliente"),
]
