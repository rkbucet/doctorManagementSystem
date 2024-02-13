from django.urls import path
from doctorApp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('insert', views.insertFun, name='insert'),
    path('update/<int:id>', views.updateFun, name='update'),
    path('delete/<int:id>', views.deleteFun, name='delete'),
]