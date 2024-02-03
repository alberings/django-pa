from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib.auth import logout

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'profiles/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'profiles/profile.html')

def custom_logout(request):
    if request.method == 'POST':
        # Perform logout using the built-in Django logout function
        logout(request)
        return redirect('home')  # Redirect to the home page after logout
    else:
        return redirect('home')  # Redirect to the home page for GET requests