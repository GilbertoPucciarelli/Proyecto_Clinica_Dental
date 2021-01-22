
from django.urls import path
from users import views


urlpatterns = [

    path(
        route = 'login/',
        view = views.LoginView.as_view(),
        name = "login",
    ),

    path(
        route = 'signup/',
        view = views.SignUpView.as_view(),
        name = "signup",
    ),

    path(
        route = 'logout/',
        view = views.LogOutView.as_view(),
        name = "logout",
    ),

    path(
        route = 'superuser/',
        view = views.SuperUserView.as_view(),
        name = "superuser",
    ),

    path(
        route = 'edit_user/<int:pk>',
        view = views.EditUserView.as_view(),
        name = "edit_user",
    ),

    path(
        route = 'statistics',
        view = views.StatisticsFeedView.as_view(),
        name = "statistics",
    ),

]