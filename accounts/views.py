from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from pages.models import TAProfile
from .forms import CustomUserCreationForm, StudentProfileForm
from django.contrib.auth.decorators import login_required
from .models import StudentProfile

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

    def form_valid(self, form):
        response = super().form_valid(form) #save new user  

        if form.cleaned_data["is_ta"]: #is registered as TA?
            ta_profile = TAProfile.objects.create( #creates TA profile
                user=self.object
            )

            ta_profile.courses.set( #save courses selected
                form.cleaned_data["courses"]
            )
        return response #login page redirect


@login_required 

def student_profile(request):
    profile, created = StudentProfile.objects.get_or_create(
        user = request.user
    )

    if request.method == "POST":
        form = StudentProfileForm(request.POST, instance=profile)

        if form.is_valid():
            form.save()
            return redirect("student_profile")
    
    else: 
        form = StudentProfileForm(instance=profile)

    return render(request, "accounts/student_profile.html", {
        "form": form
    })
