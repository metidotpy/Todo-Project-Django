from django.shortcuts import redirect
class ReturnIfAuthenticateMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('todo:home')
        else:
            return super().dispatch(request, *args, **kwargs)