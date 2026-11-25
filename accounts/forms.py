from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, StudentProfile
from django import forms
from pages.models import Course


class CustomUserCreationForm(UserCreationForm):
    #is_ta: designates TA assignment
    #is_ta = forms.BooleanField(
        #required=False,
        #label="Register as a Teaching Assistant"
    #)
    #courses displays available courses
   # courses = forms.ModelMultipleChoiceField(
       # queryset=Course.objects.all(),
       # widget=forms.CheckboxSelectMultiple,
       # required=False,
       # label="Courses You Can Tutor"
    #)
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "display_name",
            "birthday",
            "email",
        )
        labels = {
            "display_name": "Display Name (you can change this later)", 
            "email": "Email Address",
        }

        widgets = {
            "birthday": forms.DateInput(attrs={"type": "date"}),
            
        }



class CustomUserChangeForm(UserChangeForm):
    password = None

    interests = forms.MultipleChoiceField(
            choices=CustomUser.INTERESTS,
            widget=forms.SelectMultiple(attrs={
                #"id": "interests-select",
                "placeholder": "Search or select interests..."
            }),
            required=False,
        )
    bio = forms.CharField(
        widget=forms.Textarea(attrs={
            "rows": 3,
            "placeholder": "Tell other students a little about yourself..."
        }),
        required=False,
    )
    certificate = forms.MultipleChoiceField(
            choices=CustomUser.CERTIFICATES,
            widget=forms.SelectMultiple(attrs={
                #"id": "interests-select",
                "placeholder": "Search or select a certificate..."
            }),
            required=False,
        )
    minor = forms.MultipleChoiceField(
            choices=CustomUser.MINORS,
            widget=forms.SelectMultiple(attrs={
                #"id": "interests-select",
                "placeholder": "Search or select a minor..."
            }),
            required=False,
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk and self.instance.interests:
            self.initial["interests"] = self.instance.interests

    


    class Meta:
        model = CustomUser
        fields = (
            "display_name",
            "email",
            "year",
            "major_type",
            "major",
            "minor",
            "certificate",
            "interests",
            "bio",
            #"friends",
            "profile_pic",
        )
        labels = {
            "display_name": "Display Name", 
            "email": "Email Address",
            "major_type": "Degree Type",
            "minor": "Minor(s)",
            "certificate": "Certificate(s)",
        }
        widgets = {
            "birthday": forms.DateInput(attrs={"type": "date"}),
        }
    def clean_interests(self):
        interests = self.cleaned_data.get("interests")
        if not interests or len(interests) < 3:
            raise forms.ValidationError("Please select at least 3 interests.")
        return interests
    
    def clean_minor(self):
        minor = self.cleaned_data.get("minor")
        if len(minor) > 3:
            raise forms.ValidationError("Please select no more than 3 minors.")
        return minor
    
    def clean_certificate(self):
        certificate = self.cleaned_data.get("certificate")
        if len(certificate) > 3:
            raise forms.ValidationError("Please select no more than 3 certificates.")
        return certificate



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
    empty_value=None,
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
