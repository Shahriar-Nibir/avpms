from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('homeAO')
            elif user.is_staff:
                return redirect('homeNCO')
            else:
                return redirect('homeDvr')
    return render(request, 'login.html')


def homeAO(request):
    return render(request, 'homeAO.html')


def homeNCO(request):
    return render(request, 'homeNCO.html')


def homeDvr(request):
    return render(request, 'homeDvr.html')


def logoutUser(request):
    logout(request)
    return redirect('loginUser')
