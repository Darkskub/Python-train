from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from datetime import datetime

from .forms import AuthUserForm, UserCreationForm

# Create your views here.
class Login(LoginView):
    fields = ["username", "password"]
    template_name = 'Users/login.html'
    form_class = AuthUserForm

class logout(LogoutView):
    template_name = 'Users/logout.html'


def register(request):
    regform = UserCreationForm(request.POST)
    if request.method == "POST":
        if regform.is_valid():
            reg_f = regform.save(commit=False)
            reg_f.is_active = True
            reg_f.is_staff = False
            reg_f.is_superuser = False
            reg_f.date_joined = datetime.now()
            reg_f.last_login = datetime.now()
            regform.save()

            reg_f.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, reg_f)
            return redirect('news:Gingerbreads')
    else:
        regform = UserCreationForm()
    return render(request, 'Users/registration.html', {"regform": regform})

def profile(request):
    user_blogs = request.user.gingerbreads_set.all()
    return render(request, 'Users/profile.html', {"user_blogs":user_blogs})


