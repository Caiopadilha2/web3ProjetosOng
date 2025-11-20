
from django.contrib.auth import views as auth_views
from django.contrib import messages

from django.urls import reverse_lazy


class LoginView(auth_views.LoginView):
    
    template_name = 'login.html'
    redirect_authenticated_user = True  
    
    def form_valid(self, form):
        """ login bem-sucedido"""
        messages.success(self.request, f'Bem-vindo(a), {form.get_user().username}!')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        """login falha"""
        messages.error(self.request, 'Usuário ou senha incorretos.')
        return super().form_invalid(form)
    


class LogoutView(auth_views.LogoutView):
    
    next_page = reverse_lazy('accounts:login')  
    
    def dispatch(self, request, *args, **kwargs):
        """antes do logout"""
        if request.user.is_authenticated:
            messages.info(request, 'Você saiu do sistema com sucesso.')
        return super().dispatch(request, *args, **kwargs)






