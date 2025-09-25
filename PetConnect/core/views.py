from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import RegisterForm
from .models import Pet

def home(request):
    return render(request, 'core/home.html')

def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('home')
    return render(request, 'core/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'core/login.html')

def user_logout(request):
    logout(request)
    return redirect('home')

def adopt(request):
    pets = Pet.objects.filter(adopted=False)
    return render(request, 'core/adopt.html', {'pets': pets})

@login_required
@user_passes_test(lambda u: u.is_staff)
def admin_dashboard(request):
    pets = Pet.objects.all()
    return render(request, 'core/admin_dashboard.html', {'pets': pets})