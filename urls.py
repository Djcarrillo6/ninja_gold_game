from django.urls import path
from . import views

# NO LEADING SLASHES
urlpatterns = [
    path('', views.index),
    path("process_money", views.process_money),
    path("reset", views.reset)

]
