from django.urls import path
from . import views

app_name = "member"
urlpatterns = [
    path('register', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('login/login_ok', views.login_ok, name='login_ok'),
    path('logout/', views.logout, name='logout'),
    path('register_ok/', views.register_ok, name='register_ok'),
    path('opinion/', views.opinion, name='opinion'),
    path('opinion_ok/', views.opinion_ok, name='opinion_ok'),
]
