from django.urls import path
from . import views

app_name = "logreg"

urlpatterns = [
    path("/", views.logreg),
    path("dashboard", views.dashboard)
]