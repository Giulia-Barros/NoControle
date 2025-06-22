from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home.html'

class CadastroView(TemplateView):
    template_name = 'cadastro.html'

class LoginView(TemplateView):
    template_name = 'login.html'

