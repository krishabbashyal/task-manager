from django.urls import path
from main import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("", login_required(views.HomeView.as_view()), name = "home"),
]
