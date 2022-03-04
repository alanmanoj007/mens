from django.contrib import admin
from . models import *
# Register your models here.
class Catadmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(categ,Catadmin)

class Prodadmin(admin.ModelAdmin):
    list_display = ['name','slug','img','desc','price','stock']
    list_editable = ['img','desc','price','stock']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(products,Prodadmin)
