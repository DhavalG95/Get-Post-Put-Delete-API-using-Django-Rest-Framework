from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',home,name="home"),
    path('register',register,name='register'),
    path('login',auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout',auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('project',project,name="project"),
    path('createproject',createproject,name="createproject"),
    path('<int:pk>',edit,name='edit'),
    path('delete/<int:pk>',delete,name='delete'),
    path('myproject',myproject,name='myproject'),
    path('clientdt',ClientDt.as_view(),name='clientdt'),
    path('clientdetail/<int:id>',ClientDetail.as_view(),name='clientdetail'),
    path('projectdt',ProjectDt.as_view(),name='projectdt'),
    path('projectdetail/<int:id>',ProjectDetail.as_view(),name='projectdetail')
    
]

