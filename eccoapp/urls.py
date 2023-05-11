from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.about, name="about"),
    path("contactus", views.contactus, name="contactus"),
    path('dashboardv1', views.dashboard, name='dashboardv1'),
    path('allusers', views.allusers, name='allusers'),
    path('addnewuser', views.addnewuser, name='addnewuser'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('forgotpassword', views.forgotpassword, name='forgotpassword'),
    path('emailverification', views.emailverification, name='emailverification'),
    path('settings', views.settings, name='settings'),

]
