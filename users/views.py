from .models import Profile
from django.shortcuts import render, redirect

# Create your views here.


def mypage(request):
    cur_user = request.user
    return render(request, "users/mypage.html", {"user": cur_user})


def edit(request):
    cur_user = request.user
    return render(request, "users/edit.html", {"user": cur_user})


def update(request):
    update_profile = request.user.profile
    update_profile.name = request.POST["name"]
    update_profile.phnum = request.POST["phnum"]
    update_profile.address = request.POST["address"]
    update_profile.save()

    return redirect("users:mypage")
