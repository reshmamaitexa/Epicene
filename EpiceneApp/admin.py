from django.contrib import admin
from .models import Login,TransUser, Institution, Job, Shelters, Officer, Med_Slot, Legal_Slot, Med_booking, Legal_booking, Event

# Register your models here.
admin.site.register(Login),
admin.site.register(TransUser)
admin.site.register(Institution)
admin.site.register(Job)
admin.site.register(Shelters)
admin.site.register(Officer)
admin.site.register(Med_Slot),
admin.site.register(Legal_Slot)
admin.site.register(Med_booking)
admin.site.register(Legal_booking)
admin.site.register(Event)

