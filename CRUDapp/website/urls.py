from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.home, name=""), 
    #path('store', views.store, name="store"),
     path('login', views.login, name="login"), 
]