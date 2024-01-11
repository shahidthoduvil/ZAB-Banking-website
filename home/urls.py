from django.urls import path,include
from .views import *
urlpatterns = [
    path('',home,name='home'),
    path('new/',newpage,name='newpage'),
    path('profile/',userprofile,name='userprofile'),
    path('get_branches/',get_branches,name='get_branches')

]
