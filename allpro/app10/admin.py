from django.contrib import admin
from app10.models import MoviesModel
# Register your models here.

class MovieModelAdmin(admin.ModelAdmin):
    list_display = ['mname','rdate','hname','hename','dname','mrating']

admin.site.register(MoviesModel,MovieModelAdmin)