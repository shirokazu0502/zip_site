from django.urls import path
from folder_zip import views


urlpatterns = [
    path("", views.index, name="folder_zip_home"),
]