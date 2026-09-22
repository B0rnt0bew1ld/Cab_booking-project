from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("<int:cab_id>", views.cab, name = "cab")
]