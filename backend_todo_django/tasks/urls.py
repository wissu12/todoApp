# accounts/urls.py
from django.urls import path
from . import views
from .views import TaskDeleteView, add_task
urlpatterns = [
    path("All/<int:user_id>/",views.get_user_tasks,name="all_tasks"),
    path("Add/",views.add_task,name="add_task"),
    path('show/<int:task_id>/', views.get_task, name='get_task'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete/<int:taskId>/', TaskDeleteView.as_view(), name='task-delete'),
    path('start/<int:task_id>/', views.start_task, name='start_task'),
    path('end/<int:task_id>/', views.end_task, name='end_task'),

]
