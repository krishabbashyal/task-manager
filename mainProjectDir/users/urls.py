from django.urls import path
from users import views

urlpatterns = [
    path("register/", views.UserView.as_view()),
]
