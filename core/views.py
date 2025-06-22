from django.contrib.auth import login
from django.db.transaction import commit
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CadastroForm, LoginForm

class HomeView(TemplateView):
    template_name = 'home.html'

class CadastroView(TemplateView):
    template_name = 'cadastro.html'

    def get(self, request, *args, **kwargs):
        form = CadastroForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cadastro realizado com sucesso!")
            return redirect('login')

        return render(request, self.template_name, {'form': form})

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
            return redirect('home')  # redireciona após o login

        return render(request, self.template_name, {'form': form})


#@login_required(login_url='login')
#from django.contrib.auth.decorators import login_required
#Acessar apenas se estiver logado