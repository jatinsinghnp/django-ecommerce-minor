

from django.views.generic import FormView

from accounts.models import ShopUser
from .forms import RegisterForm, LoginForm
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model, login
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

# Create your views here.


class RegisterPageView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('root:home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)

        return super(RegisterPageView, self).form_valid(form)

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('root:home')
        return super(RegisterPageView, self).get(request, *args, **kwargs)


class LoginPageView(LoginView):
    template_name = 'signin.html'

    form_class = LoginForm
    authentication_form = LoginForm

    def form_valid(self, form):

        remember_me = form.cleaned_data['remember_me']

        login(self.request, form.get_user())

        if remember_me:

            self.request.session.set_expiry(1209600)

        return super(LoginView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('root:home')

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('root:home')
        return super().get(request, *args, **kwargs)


class SingOutview(LogoutView):
    
    next_page='registerpage:login'
    

