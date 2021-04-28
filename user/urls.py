from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListCreateUserView.as_view()),
    path('<int:pk>', views.UpdateDeleteUserView.as_view()),
]