from django.urls import path
from . import views

app_name = "logreg"

urlpatterns = [
    path("", views.logreg),
    path("validate", views.validate),
    path("dashboard", views.dashboard),
    path("logout", views.logout)
]