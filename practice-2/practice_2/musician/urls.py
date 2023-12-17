from django.urls import path
from . import views


urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="user_logout"),
    # path("edit_musician/<int:id>", views.edit_musician, name="edit_musician"),
    path("edit_musician/", views.edit_musician, name="edit_musician"),
]
