from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .forms import LoginForm

# Create your views here.
@require_http_methods(["GET"])
def index(request):
    if not request.user.is_authenticated:
        login_form=LoginForm().as_table()
        return render(request,"login.htm",{"form": login_form})
    
    return render(request,"chat.htm")




@require_http_methods(["GET","POST"])
def login_view(request):
    if request.user.is_authenticated:
            return redirect("/")


    if request.method == "GET":
        login_form=LoginForm().as_table()
        return render(request,"login.htm",{"form": login_form})


    if request.method == "POST":
        form_data=LoginForm(request.POST)
        
        if form_data.is_valid():
            print(form_data.cleaned_data["username"],form_data.cleaned_data["password"])
            user=authenticate(request,username=form_data.cleaned_data["username"], password=form_data.cleaned_data["password"])
            if user:
                # print(user)
                login(request,user)
                return redirect("/")
            else:
                return HttpResponse("wrong username and password")



def logout(request):
    logout(request)

    return render(request,"/login")