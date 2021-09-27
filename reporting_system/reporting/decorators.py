from django.shortcuts import redirect
from reporting.models import MyUser
# from django.http import HttpResponse

def signin_required(func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("signin")
        else:
            return func(request,*args,**kwargs)

    return wrapper

def admin_permission_required(func):
    def wrapper(request,*args,**kwargs):

        if not request.user.is_admin or request.user.is_superuser:
            return redirect("signin")
        else:
            return func(request,*args,**kwargs)

    return wrapper


# def admin_permission_required(func):
#     def wrapper(request,*args,**kwargs):
#         if not request.user.is_superuser:
#             print(request.user.role)
#             return redirect("signin")
#         elif request.user.is_admin:
#             return redirect("adminhome")
#         else:
#             return func(request,*args,**kwargs)
#
#     return wrapper

# def admin_permission_required(allowed_role = []):
#     def decorator(func):
#         def wrapper(request, *args, **kwargs):
#             user_role = MyUser.objects.get(email=request.user)
#             print(user_role.role)
#             if user_role.role in allowed_role:
#                 return func(request, *args, **kwargs)
#             else:
#                 return HttpResponse('unauthorised person')
#         return wrapper
#     return decorator