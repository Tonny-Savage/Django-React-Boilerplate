  
from django.urls import path,include

from .views import TaskList,TaskDetail



urlpatterns = [
    path("",TaskList.as_view()),
    path("detail/<int:pk>/",TaskDetail.as_view()),
]