from django.contrib.auth import login
from django.views.generic import TemplateView, CreateView, UpdateView, DetailView, View, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import CadastroForm, LoginForm, TarefaForm
from .models import Tarefa

#Exibe da página Home
class HomeView(TemplateView):
    template_name = 'home.html'

#Exibe a página Cadastro e processa o formulário de cadastro do usuário
class CadastroView(TemplateView):
    template_name = 'cadastro.html'

    #Exibe o formulário
    def get(self, request, *args, **kwargs):
        form = CadastroForm()
        return render(request, self.template_name, {'form': form})

    #Processa os dados
    def post(self, request, *args, **kwargs):
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cadastro realizado com sucesso!")
            return redirect('login')

        return render(request, self.template_name, {'form': form})

#Exibe a página de Login e processa o formulário de login
class LoginView(TemplateView):
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)

        if form.is_valid():
            login(request, form.usuario)
            messages.success(request, 'Login realizado com sucesso!')
            return redirect('tarefas')  # redireciona após o login

        return render(request, self.template_name, {'form': form})

#Exibe a lista de tarefas do usuário apenas se ele estiver logado
class ListaTarefasView(LoginRequiredMixin, TemplateView):
    template_name = 'tarefas.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        filtro = self.request.GET.get('filtro', 'todas')

        if filtro == 'pendentes':
            tarefas = Tarefa.objects.filter(user=self.request.user, concluida=False)
        elif filtro == 'concluidas':
            tarefas = Tarefa.objects.filter(user=self.request.user, concluida=True)
        else:
            tarefas = Tarefa.objects.filter(user=self.request.user)

        context['tarefas'] = tarefas
        context['form'] = TarefaForm()
        context['filtro'] = filtro
        return context

#Criar uma nova tarefa
class CriarTarefaView(LoginRequiredMixin, CreateView):
    template_name = 'tarefas.html'
    model = Tarefa
    form_class = TarefaForm
    success_url = reverse_lazy('tarefas')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

#Editar uma tarefa já cadastrada
class AtualizarTarefaView(LoginRequiredMixin, UpdateView):
    template_name = 'tarefas.html'
    model = Tarefa
    form_class = TarefaForm
    success_url = reverse_lazy('tarefas')

    def get_queryset(self):
        return Tarefa.objects.filter(user=self.request.user)

#Deletar uma tarefa cadastrada
class DeletarTarefaView(LoginRequiredMixin, DeleteView):
    template_name = 'tarefas.html'
    model = Tarefa
    success_url = reverse_lazy('tarefas')

    def get_queryset(self):
        return Tarefa.objects.filter(user=self.request.user)

#Alterar o status da tareda, conluída ou não
class AlternarStatusTarefaView(LoginRequiredMixin, View):
    def post(self, request, pk):
        tarefa = get_object_or_404(Tarefa, pk=pk, user=request.user)
        tarefa.concluida = not tarefa.concluida
        tarefa.save()
        return redirect('tarefas')
