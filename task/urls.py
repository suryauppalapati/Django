from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('updateTask/<str:pk>/', views.updateTask, name='update'),
    path('deleteTask/<str:pk>/', views.deleteTask, name='delete'),
]
