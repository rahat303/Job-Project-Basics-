from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from app.models import *

def homePage(req):
    return render(req,"HomePage.html")

def LoginPage(req):
    if req.method == "POST":
        user_name=req.POST.get('user_name')
        pass_word=req.POST.get('pass_word')

        user=authenticate(username=user_name,password=pass_word)

        if user:
            login(req,user)
            return redirect("homePage")
        else:
            return HttpResponse("Your user information is wrong")
    return render(req,"Authentication\LoginPage.html")

def LogoutPage(req):
    logout(req)
    return render(req,"HomePage.html")

def SignUpPage(req):
    if req.method == "POST":
        user_type = req.POST.get("user_type")
        username = req.POST.get("username")
        display_name = req.POST.get("display_name")
        email = req.POST.get("email")
        pass_word = req.POST.get("password")
        confirm_password = req.POST.get("confirm_password")

        if pass_word == confirm_password:
            User=CustomUser.objects.create_user(
                user_type = user_type,
                username = username,
                display_name = display_name,
                email = email,
                password = pass_word
            )
            if user_type == "recruiter":
                RecruiterProfile.objects.create(user=User)
            elif user_type == "seeker":
                SeekerProfile.objects.create(user=User)
            User=authenticate(username=username,password=pass_word)

            if User:
                login(req,User)
                return redirect("homePage")
            else:
                return HttpResponse("Your user information is wrong")
        else:
            return HttpResponse("Your password and confirm password did not match")
    return render(req,"Authentication\SignUpPage.html")

@login_required
def ProfilePage(req):
    return render(req,"User_profile\ProfilePage.html")

@login_required
def edit_profile(req):
    CU = req.user
    if CU.user_type == "recruiter":
        if req.method == "POST":
            CU.display_name=req.POST.get("DisplayName")
            CU.email=req.POST.get("Email")
            CU.save()
            RP = RecruiterProfile.objects.get(user=CU)
            RP.contract_number=req.POST.get("ContractNumber")
            RP.bio=req.POST.get("Bio")
            if req.FILES.get("Profile_Picture"):
                RP.profile_pic=req.FILES.get("Profile_Picture")
            RP.save()
            return redirect("ProfilePage")
    elif CU.user_type == "seeker":
        
        seeker_data = SeekerProfile.objects.get(user=CU)

        if req.method == "POST":
            CU.display_name=req.POST.get("DisplayName")
            CU.email=req.POST.get("Email")
            
            RP = SeekerProfile.objects.get(user=CU)
            RP.contract_number=req.POST.get("ContractNumber")
            RP.web_site=req.POST.get("WebsiteUrl")
            RP.skill=req.POST.get("skills")
            if req.FILES.get("Profile_Picture"):
                RP.profile_pic=req.FILES.get("Profile_Picture")
            CU.save()
            RP.save()
            return redirect("ProfilePage")
    context = {
                'seeker_data':seeker_data,
            }
    return render(req,"User_profile\edit_profile.html", context)
