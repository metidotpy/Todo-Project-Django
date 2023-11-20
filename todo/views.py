from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, CreateView, UpdateView, DeleteView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Todo
from .forms import TodoForm

# Create your views here.


class TodoHome(LoginRequiredMixin, View):
  template_name = "todo/index.html"
  form_class = TodoForm
  success_url = "todo:home"
  
  def get(self, request, *args, **kwargs):
    form = self.form_class
    todos = Todo.objects.filter(user=self.request.user)
    context = {
      'form': form,
      'todos': todos,
    }
    return render(request, self.template_name, context)
  
  def post(self, request, *args, **kwargs):
    todos = Todo.objects.all()
    form = self.form_class(request.POST)
    if form.is_valid():
      text = form.cleaned_data['text']
      todo = Todo.objects.create(text=text, user = self.request.user)
      todo.save()
      todos = Todo.objects.filter(user=self.request.user)
      return redirect(self.success_url)
    return render(request, self.template_name, {"form": form, "todos": todos})

class TodoUpdateView(LoginRequiredMixin, UpdateView):
  model = Todo
  # fields = ['text']
  form_class = TodoForm
  template_name = 'todo/update_todo.html'
  success_url = reverse_lazy('todo:home')

class TodoDeleteView(LoginRequiredMixin, DeleteView):
  model = Todo
  template_name = 'todo/accept_delete.html'
  success_url = reverse_lazy('todo:home')

def change_todo(request, pk):
  todo = Todo.objects.get(pk=pk)
  todo.is_done = not todo.is_done
  todo.save()
  
  return redirect('todo:home')