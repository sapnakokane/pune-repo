from django.contrib import admin
from app12.models import tempfil
# Register your models here.
class tempfilAdmin(admin.ModelAdmin):
    list_display = ['name','age','date','img','sal']

admin.site.register(tempfil,tempfilAdmin)
