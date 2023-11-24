from django.contrib import admin

from .models import User,Detailer,Checker

admin.site.register(User)
admin.site.register(Detailer)
admin.site.register(Checker)