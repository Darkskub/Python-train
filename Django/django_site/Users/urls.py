from django.urls import path
from . import views

app_name = "Users"

urlpatterns = [
    path("login/", views.Login.as_view(), name="login"),
    path("logout/", views.logout.as_view(), name="logout"),
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),
]
