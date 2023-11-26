from django.contrib import admin

from .models import User,Detailer,Checker,Client

admin.site.register(User)
# admin.site.register(Detailer)

@admin.register(Detailer)
class DetailerAdmin(admin.ModelAdmin):
    list_display = ("name", "phone")
    
@admin.register(Checker)
class CheckerAdmin(admin.ModelAdmin):
    list_display = ("name", "phone")
    
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("name", "phone","email")