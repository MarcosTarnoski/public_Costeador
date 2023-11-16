from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def signin(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return render(request, "home.html")
        else:
            return render(request, "signin.html")
    else:
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        if user is None:
            # Si el usuario no es válido
            return render(request, "signin.html",{
                "error":"Usuario o contraseña incorrectos"
            })            
        else:
            # Si el usuario es válido
            # Primero inicio la sesión
            login(request, user)
            # Segundo redirecciono al usuario
            return redirect("home")

def signout(request):
    logout(request)
    return redirect("signin")