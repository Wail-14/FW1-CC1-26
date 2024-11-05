from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'), 
    path("collection/<int:n>", views.collection, name ="collection"),
    path ("all", views.colleclist , name ="colleclist"),
]