from django.contrib import admin
from app9.models import smodl
# Register your models here.
class smodlAdmin(admin.ModelAdmin):
    list_display = ['name','age','email']

admin.site.register(smodl,smodlAdmin)