from django.urls import path
from .views import HomeView, CadastroView, LoginView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', CadastroView.as_view(), name='cadastro'),
    path('cadastro', LoginView.as_view(), name='login'),
]