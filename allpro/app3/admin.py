from django.contrib import admin
from app3.models import mymodl
# Register your models here.

class mymodlAdmin(admin.ModelAdmin):
    list_display = ['name','age','email','date']

admin.site.register(mymodl,mymodlAdmin)