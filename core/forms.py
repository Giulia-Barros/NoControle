from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Tarefa

class CadastroForm(forms.ModelForm):
    senha = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput(attrs={'class': 'form-control rounded-pill', 'placeholder': 'Senha'})
    )
    confirmar_senha = forms.CharField(
        label="Confirmação de Senha",
        widget=forms.PasswordInput(attrs={'class': 'form-control rounded-pill', 'placeholder': 'Confirmação de Senha'})
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        labels = {
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'email': 'Email',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control rounded-pill', 'placeholder': 'Nome'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control rounded-pill', 'placeholder': 'Sobrenome'}),
            'email': forms.EmailInput(attrs={'class': 'form-control rounded-pill', 'placeholder': 'Email'}),
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError("Este e-mail já está em uso.")
        return email

    def clean_confirmar_senha(self):
        senha = self.cleaned_data.get('senha')
        confirmar = self.cleaned_data.get('confirmar_senha')
        if senha and confirmar and senha != confirmar:
            raise ValidationError("As senhas não coincidem.")
        return confirmar

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']  # usa o e-mail como username
        user.set_password(self.cleaned_data['senha'])
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control rounded-pill', 'placeholder': 'Email'})
    )
    senha = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={'class': 'form-control rounded-pill', 'placeholder': 'Senha'})
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        senha = cleaned_data.get('senha')

        if email and senha:
            user = User.objects.filter(email=email).first()
            if user:
                usuario = authenticate(username=user.username, password=senha)
                if usuario is not None:
                    self.usuario = usuario
                    return cleaned_data
            raise forms.ValidationError("E-mail ou senha inválidos.")
        return cleaned_data

class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ['descricao']
        widgets = {
            'descricao': forms.TextInput(attrs={
                'class': 'form-control rounded-pill',
                'placeholder': 'Digite a nova tarefa'
            })
        }
