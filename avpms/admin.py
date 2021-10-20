from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Driver)
admin.site.register(NCO)
admin.site.register(Officer)
admin.site.register(Vehicle)
admin.site.register(Daily_report)
admin.site.register(Daily_state)


admin.site.site_header = "AVPMS"
admin.site.site_title = "AVPMS"
admin.site.index_title = "AVPMS"
