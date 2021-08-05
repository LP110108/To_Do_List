"""todo_list URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp.views import main, ToDoView, TaskView, ToDoCreate, TaskDeleteView, TaskUpdate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name="main"),
    path('create/', ToDoCreate.as_view()),
    path('view/', ToDoView.as_view(), name='view'),
    path('view/task/<int:task_pk>/', TaskView.as_view(), name='task_view'),
    path('view/task/<int:pk>/delete/', TaskDeleteView.as_view(), name='article_delete'),
    path('view/task/<int:pk>/update/', TaskUpdate.as_view(), name='article_update'),
]
