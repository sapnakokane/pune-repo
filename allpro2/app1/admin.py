from django.contrib import admin
from app1.models import Emp
# Register your models here.

class EmpModel(admin.ModelAdmin):
    list_display = ['name','location','ceo']

admin.site.register(Emp,EmpModel)
