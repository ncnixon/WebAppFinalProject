from django.urls import path, include
from .views import SignUpView, student_profile, finish_acc_setup

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("profile/", student_profile, name="student_profile"),
    path("finish-setup/", finish_acc_setup, name="finish_acc_setup"),
]
