from django.urls import path
from .views import Register,signin,home,Logout,usermanager

urlpatterns = [
    path('',Register,name='register'),
    path('home/',home,name='home'),
    path('signin/',signin,name='login'),
    path('users/',usermanager,name='usermanager'),
    path('logout/',Logout,name='Logout')
]