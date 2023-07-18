from django.urls import path
from . import views
urlpatterns = [
    path("", views.index_view, name="index"),
    path("load/", views.load_view, name="load"),
]
