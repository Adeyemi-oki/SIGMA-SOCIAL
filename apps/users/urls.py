from django.urls import path

from .views import (
    delete_registered_user,
    home,
    login_view,
    logout_view,
    register,
    registered_users_admin,
)

urlpatterns = [
    path("", home, name="home"),
    path("register/", register, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("staff/users/", registered_users_admin, name="registered_users_admin"),
    path("staff/users/<int:user_id>/delete/", delete_registered_user, name="delete_registered_user"),
]
