from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, StudentProfile
from django import forms
from pages.models import Course


class CustomUserCreationForm(UserCreationForm):
    #is_ta: designates TA assignment
    is_ta = forms.BooleanField(
        required=False,
        label="Register as a Teaching Assistant"
    )
    #courses displays available courses
    courses = forms.ModelMultipleChoiceField(
        queryset=Course.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Courses You Can Tutor"
    )
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email", 
            "age",
        )

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "age",
        )

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = (
            "display_name",
            "major",
            "graduation_year",
            "bio", 
            "interests"
        )