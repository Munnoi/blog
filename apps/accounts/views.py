from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

User = get_user_model()


def login_view(request):
    if request.method == "POST":
        # Getting the 'email' and 'password' from the submitted form
        email = request.post.get("email")
        password = request.post.get("password")

        user = authenticate(
            request, username=email, password=password
        )  # Authenticating whether the credentials match. If didn't match `authenticate` returns 'None'
        if user:
            login(request, user)  # Creating a session with the user credentials
            return redirect("home")
        else:
            messages.error(
                request, "Invalid email or password"
            )  # Error send to the template 'login.html'

    return render(request, "accounts/login.html")


def register_view(request):
    if request.method == "POST":
        # Getting the 'email', 'password' and 'password2' from the submitted form
        email = request.post.get("email")
        password = request.post.get("password")
        password2 = request.post.get("password2")

        # Basic validation
        if not email or not password or not password2:
            messages.error(request, "All fields are required")
            return redirect("register")

        # Password match check
        if password != password2:
            messages.error(request, "Passwords don't match")
            return redirect("register")

        # Email uniqueness check
        if User.objects.filter(email=email).exits():
            messages.error(request, "Email already registered")
            return redirect("register")

        User.objects.create_user(email=email, password=password)

        messages.success(request, "Account created successfully")
        return redirect("login")
    return render(request, "accounts/register.html")


@login_required
def logout_view(request):
    logout(request)  # Deletes session data
    messages.success(request, "You have been logged out successfully")
    return redirect("login")
