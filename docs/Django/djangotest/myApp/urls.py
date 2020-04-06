from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('grades/', views.grades),
    path('students', views.students)
]