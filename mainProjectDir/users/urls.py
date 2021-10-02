from django.urls import path
from users import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.HomePageView.as_view(), name = "home"),
    path("register/", views.UserView.as_view(), name = "register"),
    path("login/", auth_views.LoginView.as_view(template_name = 'users/loginPage.html'), name = "login"),
    path("logout/", auth_views.LogoutView.as_view(template_name = 'users/logoutPage.html'), name = "logout"),
]
