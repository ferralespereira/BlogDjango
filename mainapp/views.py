from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    return render(request, 'mainapp/index.html', {
        'title': 'Home'
    })

def about(request):
    return render(request, 'mainapp/about.html', {
        'title': 'About'
    })

def register_page(request):
    
    register_form = UserCreationForm()

    if request.method == 'POST':
        register_form = UserCreationForm(request.POST)
    
    if register_form.is_valid():
        register_form.save()

        return redirect('index')

    return render(request, 'users/register.html', {
        'title': 'Register',
        'register_form': register_form
    })