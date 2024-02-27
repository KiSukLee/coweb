from django.urls import path
from . import views

app_name = "logreg"

urlpatterns = [
    path("logreg", views.logreg),
    path("validate", views.validate),
    path("dashboard", views.dashboard),
    path("account", views.account),
    path("logout", views.logout)
]