from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request, "home.html")

def signup(request):

    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            print("-----------------------------")
            #print(request.POST)
            try:
                user = User.objects.get(username=request.POST["username"])
                return render(request, "signup.html", {"message": "El usuario ya existe",
                "form": UserCreationForm})
            except User.DoesNotExist:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"]
                )
                user.save()
            return render(request, "home.html", {"message": "Usuario no existe"})

        return render(request, "signup.html", { "message": "Las contraseñas no coinciden",
        "form": UserCreationForm})
        # form = UserCreationForm(request.POST)
        # if form.is_valid():
        #     form.save()

    elif request.method == "GET":
        print("GET method")
        return render(request, "signup.html", {"form": UserCreationForm})
