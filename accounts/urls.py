from django.contrib.auth.views import (
    LogoutView, 
    PasswordChangeView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from django.urls import path, reverse_lazy
from . import views


app_name = 'accounts'
urlpatterns = [
    path("login/", views.LoginView.as_view(), name='login'),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("signup/", views.RegisterView.as_view(), name='signup'),
    path("password/change/", PasswordChangeView.as_view(template_name="accounts/password_change_form.html", success_url = reverse_lazy("todo:home")), name='password_change'),
]
