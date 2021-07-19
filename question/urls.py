from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.make_question, name="create"),
    path('detail/<int:id>/', views.detail, name="detail"),
    path('edit/<int:id>/', views.edit, name="edit"),
    path('delete/<int:id>/', views.delete, name="delete"),    
]