from django.contrib import admin
from carinfo.models import carinfo
class djangoAdmin(admin.ModelAdmin):
    list_display=('carName','carImages','fuleType','seats','trasmission','carRent','location','carType')
admin.site.register(carinfo,djangoAdmin)