from django.urls import path, include
from . import views

app_name = 'movieapp'
urlpatterns = [
    path('movie/<int:movie_id>/', views.Details, name='Details'),
    path('add/', views.AddMovie, name='AddMovie'),
    path('update/<int:id>/', views.Update, name='Update'),
    path('delete/<int:dele_id>/', views.Delete, name='Delete'),
    path('register/', views.Registration1, name='register'),
    path('login/', views.Login, name='login'),
    path('logout/', views.LogOut, name='logout'),
    path('', views.MyMovie, name='MyMovie'),
]
