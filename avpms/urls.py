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
]
