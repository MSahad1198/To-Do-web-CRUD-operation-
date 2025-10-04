from django.urls import path
from . import views

urlpatterns = [
    path ('addTask/', views.addTask, name = 'addTask'),
    
    #mark done
    path ('markComplete/<int:pk>/', views.markComplete, name = 'markComplete'),
    
    #mark undone
    path ('Undone/<int:pk>/', views.Undone, name = 'Undone'), 

    #edit feature
    path ('edit/<int:pk>/', views.editTask, name = 'editTask'),
]