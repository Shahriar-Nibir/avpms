from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import *
from datetime import datetime as dt
from datetime import date, timedelta
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


def vehDetail(request):
    veh = Vehicle.objects.all()
    context = {'veh': veh}
    return render(request, 'vehDetail.html', context)


def requestVeh(request):
    form = RequestVehicleForm()
    if request.method == 'POST':
        form = RequestVehicleForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('pendingReq')
    context = {'form': form}
    return render(request, 'requestVeh.html', context)\



def pendingReq(request):
    pending = Daily_report.objects.filter(qm_permission=False)
    approved = Daily_report.objects.filter(qm_permission=True)
    context = {'pending': pending, 'approved': approved}
    return render(request, 'pendingReq.html', context)


def approve(request, pk):
    pr = Daily_report.objects.get(id=pk)
    pr.qm_permission = True
    pr.save()
    return redirect('pendingReq')


def ncos(request):
    ncos = NCO.objects.all()
    context = {'ncos': ncos}
    return render(request, 'ncos.html', context)


def dailyReport(request):
    today = dt.today()
    dr = Daily_report.objects.filter(date=today, qm_permission=True)
    context = {'dr': dr}
    return render(request, 'dailyreport.html', context)


def nextdayduty(request):
    user = request.user
    driver = Driver.objects.get(user=user)
    tomorrow = date.today() + timedelta(days=1)
    duties = Daily_report.objects.filter(
        date=tomorrow, qm_permission=True, driver=driver)
    context = {'duties': duties}
    return render(request, 'nextdayduty.html', context)


def repairvehicle(request):
    form = RepairVehicleForm()
    if request.method == 'POST':
        form = RepairVehicleForm(request.POST)
        if form.is_valid():
            rv = form.save()
            v = rv.vehicle
            try:
                last = RepairVehicle.objects.filter(
                    vehicle=v).order_by('-id')[1]
                rv.last_repair_date = last.repair_date
                rv.save()
            except:
                last = None
            return redirect('homeNCO')
    context = {'form': form}
    return render(request, 'repairvehicle.html', context)


def handingtaking(request):
    user = request.user
    nco = NCO.objects.get(user=user)
    form = NCOForm()
    if request.method == 'POST':
        form = NCOForm(request.POST)
        if form.is_valid():
            new = form.save()
            phone = new.phone_no
            date = new.from_date
            logout(request)
            nco.user = None
            nco.to_date = date
            nco.save()
            user.set_password(phone)
            user.save()
            new.user = user
            new.save()

            return redirect('loginUser')
    context = {'form': form, 'nco': nco}
    return render(request, 'handingtaking.html', context)


def addpol(request):
    form = POLForm()
    if request.method == 'POST':
        form = POLForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pol')
    context = {'form': form}
    return render(request, 'addpol.html', context)


def pol(request):
    pol = POL.objects.all()
    context = {'pol': pol}
    return render(request, 'pol.html', context)
