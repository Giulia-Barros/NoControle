from django.db.transaction import commit
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CadastroForm

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
            cadas = form.save(commit=False)

            print(f'Nome: {cadas.first_name}')
            print(f'Sobrenome: {cadas.last_name}')
            print(f'Email: {cadas.email}')
            print(f'Senha: {form.cleaned_data["senha"]}')
            print(f'ConfSenha: {form.cleaned_data["confirmar_senha"]}')
            # cadas.save()
        return render(request, self.template_name, {'form': form})


class LoginView(TemplateView):
    template_name = 'login.html'



