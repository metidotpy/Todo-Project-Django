from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .forms import UserForm
from .mixins import ReturnIfAuthenticateMixin
from django.urls import reverse_lazy

# Create your views here.

class LoginView(ReturnIfAuthenticateMixin, LoginView):
  template_name = 'accounts/login.html'
  success_url = reverse_lazy("todo:home")
  redirect_authenticated_user = True

class RegisterView(ReturnIfAuthenticateMixin, CreateView):
  template_name = 'accounts/signup.html'
  form_class = UserForm
  success_url = reverse_lazy('todo:home')
  
  # def form_valid(self, form):
      
  #     return super().form_valid(form)
  