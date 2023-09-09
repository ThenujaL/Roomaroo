from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_ListCreate_View),
    path('<str:pk>/update/', views.task_update_view),
    path('<str:pk>/delete/', views.task_delete_view),
    path('<str:pk>/', views.task_details_view)
]