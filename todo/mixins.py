from django.shortcuts import redirect
from .models import Todo

class HomeIfNotUserMixin():
    def dispatch(self, request, pk, *args, **kwargs):
        todo = Todo.objects.get(pk=pk)
        if todo and todo.user == request.user:
            return super().dispatch(request, pk, *args, **kwargs)
        
        return redirect("todo:home")