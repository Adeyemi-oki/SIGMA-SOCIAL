from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

User = get_user_model()


def register(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful. Please log in.")
            return redirect("login")
    else:
        form = UserCreationForm()

    return render(request, "users/register.html", {"form": form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm(request)

    return render(request, "users/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("login")


@login_required(login_url="login")
def home(request):
    return render(request, "users/home.html")


@staff_member_required(login_url="login")
def registered_users_admin(request):
    users = User.objects.only(
        "id",
        "username",
        "email",
        "is_staff",
        "is_superuser",
        "is_active",
        "date_joined",
    ).order_by("-date_joined")
    return render(request, "users/registered_users_admin.html", {"registered_users": users})


@staff_member_required(login_url="login")
@require_POST
def delete_registered_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if user == request.user:
        messages.error(request, "You cannot remove your own admin account from this page.")
        return redirect("registered_users_admin")

    username = user.get_username()
    user.delete()
    messages.success(request, f"Removed user {username}.")
    return redirect("registered_users_admin")
