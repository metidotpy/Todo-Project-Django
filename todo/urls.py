from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.TodoHome.as_view(), name='home'),
    path('update/<int:pk>/', views.TodoUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.TodoDeleteView.as_view(), name='delete'),
    path('change/<int:pk>/', views.ChangeTodoView.as_view(), name='change'),
]
