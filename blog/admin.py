from django.contrib import admin
from .models import *

class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_date', )
    list_filter = ("name",'created_date')
    search_fields = ['name', 'cnic',]

admin.site.register(Profile,PostAdmin)


class InstallAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', )
    list_filter = ("user",'date')
    search_fields = ['user', ]

admin.site.register(Installament,InstallAdmin)