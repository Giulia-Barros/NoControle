from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import (
HomeView, CadastroView, LoginView,
ListaTarefasView, CriarTarefaView, AtualizarTarefaView,
DeletarTarefaView, AlternarStatusTarefaView
)

urlpatterns = [
# Rotas Principais
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('cadastro/', CadastroView.as_view(), name='cadastro'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
# Rotas de tarefas
    path('tarefas/', ListaTarefasView.as_view(), name='tarefas'),
    path('tarefas/criar/', CriarTarefaView.as_view(), name='criar_tarefa'),
    path('tarefas/<int:pk>/editar/', AtualizarTarefaView.as_view(), name='editar_tarefa'),
    path('tarefas/<int:pk>/deletar/', DeletarTarefaView.as_view(), name='deletar_tarefa'),
    path('tarefas/<int:pk>/alternar/', AlternarStatusTarefaView.as_view(), name='alternar_tarefa'),
]

