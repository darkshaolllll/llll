from django.contrib import admin
from .models import person
# Register your models here.
class Person_manage(admin.ModelAdmin):
    list_display=['id','name','age']
admin.site.register(person,Person_manage)