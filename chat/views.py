from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.models import User

from .forms import LoginForm

# Create your views here.
@require_http_methods(["GET"])
def index(request):
    print(request.user)
    login_form=LoginForm().as_table()
    return render(request,"login.htm",{"form": login_form})




@require_http_methods(["GET","POST"])
def login(request):
    print(request.session)
    if request.method == "GET":
        users=User.objects.all()
        print(users)
        return HttpResponse("login")

    if request.method == "POST":
        username=request.POST["username"]
        password = request.POST["password"]
        print(username,password)
        user=User.objects.filter(username=username)
        print(user)
        return redirect('/')