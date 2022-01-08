from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),?
    path('loginUser', views.loginUser, name='loginUser'),
    path('logoutUser', views.logoutUser, name='logoutUser'),
    path('homeAO', views.homeAO, name='homeAO'),
    path('homeNCO', views.homeNCO, name='homeNCO'),
    path('homeDvr', views.homeDvr, name='homeDvr'),
    path('vehDetail', views.vehDetail, name='vehDetail'),
    path('requestVeh', views.requestVeh, name='requestVeh'),
    path('pendingReq', views.pendingReq, name='pendingReq'),
    path('approve/<str:pk>', views.approve, name='approve'),
    path('ncos', views.ncos, name='ncos'),
    path('dailyReport', views.dailyReport, name='dailyReport'),
    path('nextdayduty', views.nextdayduty, name='nextdayduty'),
    path('repairvehicle', views.repairvehicle, name='repairvehicle'),
    path('handingtaking', views.handingtaking, name='handingtaking'),
    path('addpol', views.addpol, name='addpol'),
    path('pol', views.pol, name='pol'),
]
