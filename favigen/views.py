<<<<<<< HEAD
from multiprocessing import context
from django.views.generic import TemplateView
from unicodedata import name
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

=======
from django.shortcuts import render, redirect
from favigen.forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import CustomUser
>>>>>>> 0fb436d51a861efdb8fa5c00db68af6f5e1be7f2

# Create your views here.
def home_page(request):
    return render(request, "favigen/home.html")


def signup_page(request):
    # if not request.user.is_anonymous:
    #     return redirect("favigen:home")

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            f_name = form.cleaned_data.get('first_name')
            messages.success(request, f"Registration successful for {f_name}")
            return redirect("favigen:home")
        messages.error(request, "Unsuccessful registration. Invalid information.")

    form = CustomUserCreationForm()
    return render (request=request, template_name="favigen/sign-up.html", context={"signup_form": form})


def login_page(request):
    user = request.user
    # if user.is_authenticated:
    #     return redirect("favigen:home")

    if request.POST:
        form    = CustomAuthenticationForm(request.POST)
        email   = request.POST.get('email')
        password = request.POST.get('password')

        if user := authenticate(email=email, password=password):
            login(request, user)
            messages.success(request, "Logged In")
            return redirect("favigen:home")
        else:
            messages.error(request, "Please enter correct details")
    else:
        form = CustomAuthenticationForm()

    context = {'login_form': form}
    return render(request, "favigen/login.html", context)

def signup_page(request):
    # if not request.user.is_anonymous:
    #     return redirect("favigen:home")

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            f_name = form.cleaned_data.get('first_name')
            messages.success(request, f"Registration successful for {f_name}")
            return redirect("favigen:home")
        messages.error(request, "Unsuccessful registration. Invalid information.")

    form = CustomUserCreationForm()
    return render (request=request, template_name="favigen/sign-up.html", context={"signup_form": form})


<<<<<<< HEAD
def login(request):
    return render(request, "favigen/login.html")

def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)
        context["url"] = fs.url(name)
    return render(request, 'favigen/upload.html', context)
    
=======
def login_page(request):
    user = request.user
    # if user.is_authenticated:
    #     return redirect("favigen:home")

    if request.POST:
        form    = CustomAuthenticationForm(request.POST)
        email   = request.POST.get('email')
        password = request.POST.get('password')

        if user := authenticate(email=email, password=password):
            login(request, user)
            messages.success(request, "Logged In")
            return redirect("favigen:home")
        else:
            messages.error(request, "Please enter correct details")
    else:
        form = CustomAuthenticationForm()

    context = {'login_form': form}
    return render(request, "favigen/login.html", context)


def logout_view(request):
    logout(request)
    messages.success(request, "Logged Out")
    return redirect("favigen:home")
>>>>>>> 0fb436d51a861efdb8fa5c00db68af6f5e1be7f2
