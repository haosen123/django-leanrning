from django.shortcuts import render
# from django.http import HttpResponse
from AppTwo.models import User
from AppTwo.forms import UserForm
from AppTwo.forms import UserProfileInfoForm
# Create your views here.

def index(request):
    return render(request,"AppTwo/index.html")

def help(request):
    my_dic = {'help_page':'Help Page'}
    return render(request,'AppTwo/help.html',context = my_dic)

def users(request):
    # u = User.objects.order_by("first_name")
    # my_dic = {'user_table':u}
    # return render(request,'AppTwo/user.html',context = my_dic)
    form = UserForm()

    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            form.save()
            return index(request)
        else:
            print("ERROR FROM INVALID")

    return render(request,"AppTwo/user.html",context = {"form":form})

def userprofile(request):
    profileform = UserProfileInfoForm

    if request.method == "POST":
        profileform = UserProfileInfoForm(request.POST)

        if profileform.is_valid():
            profileform.save()
            return index(request)

    return render(request,'AppTwo/profileform.html',context = {"profileform":profileform})
