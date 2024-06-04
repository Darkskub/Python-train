from django.urls import path
from . import views

app_name="news"
urlpatterns = [
    path("", views.index, name="Gingerbreads"),
    path("news/", views.news, name="News"),
    path("contacts/", views.contacts, name="contacts"),
    path("detail/<int:pk>/", views.detail, name="Gingerbreads_detail"),
    path("create/",views.create_news , name="create_news"),
]