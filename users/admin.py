from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Startup, Investor, Person, Industry, Sector, Status, Job, Type, Pub_or_priv, Field, Status_interest


# Register your models here.



admin.site.register(Job)
admin.site.register(Type)
admin.site.register(User, UserAdmin)
admin.site.register(Startup)
admin.site.register(Investor)
admin.site.register(Person)
admin.site.register(Industry)
admin.site.register(Sector)
admin.site.register(Status)

admin.site.register(Pub_or_priv)
admin.site.register(Field)
admin.site.register(Status_interest)
