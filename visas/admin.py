from django.contrib import admin
from visas.models import contact,Schedule

class ContactAdmin(admin.ModelAdmin):
    list_display=('email','subject','message')

class ScheduleAdmin(admin.ModelAdmin):
    list_display=('email','subject','message')


# Register your models here.
admin.site.register(contact,ContactAdmin)
admin.site.register(Schedule,ScheduleAdmin)