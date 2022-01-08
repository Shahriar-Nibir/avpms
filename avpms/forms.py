from django.db.models import fields
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *


class RequestVehicleForm(ModelForm):
    class Meta:
        model = Daily_report
        fields = ['vehicle', 'driver', 'date', 'RV', 'out_time', 'reason']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'out_time': forms.TimeInput(attrs={'type': 'time'})
        }


class RepairVehicleForm(ModelForm):
    class Meta:
        model = RepairVehicle
        fields = ['vehicle', 'number', 'info', 'repair_date', 'vehicle_model']
        widgets = {
            'repair_date': forms.DateInput(attrs={'type': 'date'}),
        }


class NCOForm(ModelForm):
    class Meta:
        model = NCO
        fields = ['snk_no', 'name', 'phone_no', 'image', 'from_date']
        widgets = {
            'from_date': forms.DateInput(attrs={'type': 'date'}),
        }


class POLForm(ModelForm):
    class Meta:
        model = POL
        fields = '__all__'
