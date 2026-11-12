from django.urls import path
from .views import SignUpView, student_profile

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("profile/", student_profile, name="student_profile"),
]