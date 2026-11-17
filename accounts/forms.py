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


    graduation_year = forms.TypedChoiceField(
    choices=[
        ("", "Select One"),
        (2026, "2026"),
        (2027, "2027"),
        (2028, "2028"),
        (2029, "2029"),
        (2030, "2030"),
        (2031, "2031"),
        (2032, "2032"),
    ],
    coerce=int,
    required=False,
    widget=forms.Select()
)

    major = forms.ChoiceField(
        choices=[
            ("", "Select One"),
            ("Accounting", "Accounting"),
            ("Anthropology", "Anthropology"),
            ("Art & Design", "Art & Design"),
            ("Biology", "Biology"),
            ("Business Administration", "Business Administration"),
            ("Communication Studies", "Communication Studies"),
            ("Computer Science", "Computer Science"),
            ("Criminology", "Criminology"),
            ("Education", "Education"),
            ("English", "English"),
            ("Environmental Science", "Environmental Science"),
            ("Finance", "Finance"),
            ("Forestry", "Forestry"),
            ("Game Design & Interactive Media", "Game Design & Interactive Media"),
            ("History", "History"),
            ("Journalism", "Journalism"),
            ("Management Information Systems", "Management Information Systems"),
            ("Marketing", "Marketing"),
            ("Mathematics", "Mathematics"),
            ("Media Arts", "Media Arts"),
            ("Music", "Music"),
            ("Nursing", "Nursing"),
            ("Philosophy", "Philosophy"),
            ("Physics", "Physics"),
            ("Political Science", "Political Science"),
            ("Psychology", "Psychology"),
            ("Public Health", "Public Health"),
            ("Social Work", "Social Work"),
            ("Sociology", "Sociology"),
            ("Wildlife Biology", "Wildlife Biology"),
            ("Undeclared", "Undeclared"),
            ("Other", "Other"),
        ],
        required=False,
        widget=forms.Select()
    )
    class Meta:
        model = StudentProfile
        fields = (
            "display_name",
            "major",
            "graduation_year",
            "bio",
            "interests",
            "looking_for",
        )

        #MSC. widget
        widgets = {
    "looking_for": forms.CheckboxSelectMultiple(),
    "interests": forms.TextInput(),
    "bio": forms.Textarea(attrs={
        "rows": 3,
        "placeholder": "Tell other students a little about yourself..."
    }),
}
