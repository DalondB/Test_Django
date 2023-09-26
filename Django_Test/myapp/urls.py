from django.urls import path
from . import views

#Configured url in myapp
#This is where all the prefixes for this application is located
urlpatterns = [
    #When we go to the path "", call the function home() in views
    path("", views.home, name="home"),
    path("todos/", views.todos, name="Todos")

    #Example: path("", views.home, name="home")
]