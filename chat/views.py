from django.shortcuts import render, redirect
from . forms import LoginForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

# Create your views here.
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request = request, data = request.POST)
        if form.is_valid:
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(username, password)
            user = authenticate(request, username=username, password=password)
            update_session_auth_hash(request, user)
            if user is not None:
                login(request, user)
                return redirect('profile')
        else:
            return redirect('/login')
    form = LoginForm()
    return render(request, 'chat/login.html', {'form': form})