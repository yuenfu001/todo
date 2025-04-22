from django.urls import path
from . import views
urlpatterns = [
    path("",views.home,name='home'),
    path("create-todo/",views.created_todo,name='create'),
    path("edit-todo/<str:todo>/",views.edit_todo,name='edit'),
    path("delete-todo/<str:delete>/",views.delete_todo,name='delete'),
    path("done-todo/<str:done>/",views.mark_done,name='done'),
]
