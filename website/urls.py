from django.urls import path
from . import views


app_name = 'website'

urlpatterns = [
    path('', views.home_page, name="home-page"),
    path('resume/', views.view_resume, name="resume-page"),
] 
