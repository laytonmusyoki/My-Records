from django.shortcuts import redirect
from django.contrib import messages


def authenticated_users(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return view_func(request,*args,**kwargs)
    return wrapper_func



def allowed_users(user_roles=[]):
    def decorator(view_func):
        def wrapper_func(request,*args,**kwargs):
            group=None
            if request.user.groups.exists():
                group=request.user.groups.all()[0].name
            if group in user_roles:
                return view_func(request,*args,**kwargs)
            else:
                messages.info(request,'You are not allowed to view adminpage')
                return redirect('home')
        return wrapper_func
    return decorator