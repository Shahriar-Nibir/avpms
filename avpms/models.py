from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    snk_no = models.CharField(
        max_length=100, null=True, blank=True, unique=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    phone_no = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(null=True, blank=True,
                              upload_to='driver_image/', default='pro_pic.png')
    avail = models.BooleanField(default=True)

    def __str__(self):
        return self.snk_no


class NCO(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    snk_no = models.CharField(
        max_length=100, null=True, blank=True, unique=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    phone_no = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='nco_image/')
    from_date = models.DateField(null=True)
    to_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.snk_no


class Officer(models.Model):
    APPT = (
        ('CO', 'CO'),
        ('2IC', '2IC'),
        ('QM', 'QM'),
        ('ADJT', 'ADJT'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    ba_no = models.CharField(max_length=100, null=True,
                             blank=True, unique=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    phone_no = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(null=True, blank=True,
                              upload_to='officer_image/')
    appt = models.CharField(max_length=100, null=True,
                            blank=True, choices=APPT)

    def __str__(self):
        return self.ba_no


class Vehicle(models.Model):
    CLASS = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
    )
    TYPE = (
        ('Jeep', 'Jeep'),
        ('Pick up', 'Pick up'),
        ('Bus', 'Bus'),
    )
    AUTHORITY = (
        ('General', 'General'),
        ('Operational', 'Operational'),
        ('Trining', 'Trining'),
    )
    ba_no = models.CharField(max_length=100, null=True, unique=True)
    vehicle_class = models.CharField(max_length=100, null=True, choices=CLASS)
    type = models.CharField(max_length=100, null=True, choices=TYPE)
    km_reading = models.PositiveBigIntegerField(null=True, blank=True)
    autority = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.ba_no


class Daily_report(models.Model):
    vehicle = models.ForeignKey(Vehicle, null=True, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, null=True, on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)
    in_time = models.TimeField(null=True, blank=True)
    out_time = models.TimeField(null=True, blank=True)
    RV = models.CharField(max_length=200, null=True, blank=True)
    reason = models.CharField(max_length=300, null=True, blank=True)
    qm_permission = models.BooleanField(default=False)

    def __str__(self):
        return self.vehicle.ba_no + str(self.date)


class Daily_state(models.Model):
    date = models.DateField(auto_now=True, null=True)
    total = models.PositiveIntegerField(null=True, blank=True)
    in_garrison = models.PositiveIntegerField(null=True, blank=True)
    out_garrison = models.PositiveIntegerField(null=True, blank=True)
    workshop = models.PositiveIntegerField(null=True, blank=True)
    garrage = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.date)


class RepairVehicle(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    number = models.CharField(max_length=100, null=True, unique=True)
    last_repair_date = models.DateField(null=True, blank=True)
    info = models.TextField(null=True, blank=True)
    repair_date = models.DateField(null=True)
    vehicle_model = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.vehicle.ba_no + str(self.repair_date)


class POL(models.Model):
    TYPE = (
        ('Petrolium', 'Petrolium'),
        ('Oil', 'Oil'),
        ('Lubricant', 'Lubricant'),
    )
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    type = models.CharField(max_length=200, null=True, choices=TYPE)
    authorised = models.PositiveIntegerField(null=True)
    stock = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.vehicle.ba_no + self.type
