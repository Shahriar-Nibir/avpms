from django.contrib import admin
from .models import *

# Register your models here.


class Daily_reportAdmin(admin.ModelAdmin):
    list_display = ['vehicle', 'driver', 'qm_permission']


admin.site.register(Driver)
admin.site.register(NCO)
admin.site.register(Officer)
admin.site.register(Vehicle)
admin.site.register(Daily_report, Daily_reportAdmin)
admin.site.register(Daily_state)
admin.site.register(RepairVehicle)
admin.site.register(POL)


admin.site.site_header = "AVPMS"
admin.site.site_title = "AVPMS"
admin.site.index_title = "AVPMS"
