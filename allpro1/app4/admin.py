from django.contrib import admin
from app4.models import SapModel
# Register your models here.
class SapModelAdmin(admin.ModelAdmin):
    list_display = ['eno','ename','esal','eaddr']

admin.site.register(SapModel,SapModelAdmin)