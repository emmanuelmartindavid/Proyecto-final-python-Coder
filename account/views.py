from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from account.forms import UserRegisterForm
from account.models import Avatar


def editar_usuario(request):
    user = request.user
    try:
        avatar = user.avatar
    except Avatar.DoesNotExist:
        avatar = None

    if request.method == "POST":
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            informacion = form.cleaned_data
            user.username = informacion["username"]
            user.email = informacion["email"]
            user.save()

            if informacion.get("imagen"):
                if avatar:
                    avatar.imagen = informacion["imagen"]
                    avatar.save()
                else:
                    avatar = Avatar(user=user, imagen=informacion["imagen"])
                    avatar.save()

            return redirect("accountLogin")

    form = UserRegisterForm(initial={
        "username": user.username,
        "email": user.email,
        "is_staff": user.is_staff,
        "imagen": avatar.imagen if avatar else None
    })

    context = {
        "form": form,
        "titulo": "Editar usuario",
        "enviar": "Editar"
    }
    return render(request, "form.html", context=context)


def register_account(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect("AppUnderArtCreateContent")

    form = UserRegisterForm()
    context = {
        "form": form,
        "titulo": "Registrar usuario",
        "enviar": "Registrar"
    }
    return render(request, "form.html", context=context)


def login_account(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            informacion = form.cleaned_data

            user = authenticate(username=informacion['username'], password=informacion['password'])
            if user is not None:
                login(request, user)

                return redirect("AppUnderArtCreateContent")
            else:
                return redirect("AppUnderArtCreateContent")

    form = AuthenticationForm()
    context = {
        "form": form,
        "titulo": "Login",
        "enviar": "Iniciar"
    }
    return render(request, "form.html", context=context)
