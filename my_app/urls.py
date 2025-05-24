from django.urls import path
from . import views

urlpatterns = [
    path('',views.task,name='task'),
    path('home/',views.home,name='home'),
    path('edit/<int:id>/',views.Edit,name='edit'),
    path('delete/<int:id>/',views.delete_todo,name='delete'),
]
