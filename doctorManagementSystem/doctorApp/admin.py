from django.contrib import admin
from doctorApp.models import Location, Speciality, Doctor


admin.site.register(Doctor)
admin.site.register(Location)
admin.site.register(Speciality)