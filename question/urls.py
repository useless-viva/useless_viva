from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.question_create, name="question_create"),
    path('<int:id>/', views.question_detail, name="question_detail"),
    path('edit/<int:id>/', views.question_edit, name="question_edit"),
    path('delete/<int:id>/', views.question_delete, name="question_delete"),    
    # path('choices/<int:id>/', views.choices, name="choices"),
]