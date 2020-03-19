from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.


class buyAdmin(admin.ModelAdmin):
    list_display=('username','size','tel_no','email','amount', 'status')
    list_filter =('username',)

class sellAdmin(admin.ModelAdmin):
    list_display=('username','id_scan','title_scan','size','reside', 'is_active')
    list_filter =('reside','size', 'username')


#admin.site.register(User, UserAdmin)
admin.site.register(buy)
admin.site.register(sell)
admin.site.register(profile)
admin.site.register(File)