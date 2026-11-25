from datetime import date
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from pages.models import TAProfile
from .forms import CustomUserCreationForm, CustomUserChangeForm, StudentProfileForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import StudentProfile, CustomUser
from django.contrib import messages

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("finish_acc_setup") #"/registration/finish_acc_setup/" #reverse_lazy("login")

    def form_valid(self, form):
        birthday = form.cleaned_data.get("birthday")

        if birthday:
            today = date.today()
            age = (
                today.year 
                - birthday.year
                - ((today.month, today.day) < (birthday.month, birthday.day))
            )
        
            if age < 16:
                return render(self.request, "registration/age_too_young.html")
        
        
        
        response = super().form_valid(form) #save new user 
        login(self.request, self.object) 

       
       
        #return render(self.request, "registration/finish_acc_setup.html")
        
        return response #login page redirect

#only registered users can access profile page
@login_required 
# Retrieve an existing profile without creating a new one.
def student_profile(request):
    profile = StudentProfile.objects.filter(
        user=request.user
    ).first()

    form = StudentProfileForm(
        request.POST or None,
        instance=profile
    )

    if request.method == "POST":

        if form.is_valid():
            student_profile = form.save(commit=False) #prepare profile without save
            student_profile.user = request.user #assc. profile with logged in user
            student_profile.save() #sqlite save
            form.save_m2m() #saves looking_for field
            messages.success(request, "Your profile was saved successfully!")
            return redirect("student_profile")
    

    return render(request, "accounts/student_profile.html", {
        "form": form
    })

@login_required
def finish_acc_setup(request):

    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)

        if form.is_valid(): 
            stuff = form.save(commit=False)
            stuff.user = request.user
            stuff.save()
            form.save()#_m2m()
            messages.success(request, "Your profile was saved successfully!")
            return redirect("home")
    else:
        #auto populate with existing profile data if available otherwise omit instance
        form = CustomUserChangeForm(instance=request.user)

    return render(request, "registration/finish_acc_setup.html", {"form": form})