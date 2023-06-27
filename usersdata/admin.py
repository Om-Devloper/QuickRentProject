from django.contrib import admin
from usersdata.models import userdata
class userAdmin(admin.ModelAdmin):
    list_display=('userName','password','email')
# Register your models here.
admin.site.register(userdata,userAdmin)
