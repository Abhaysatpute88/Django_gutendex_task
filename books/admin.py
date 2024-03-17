from django.contrib import admin
from .models import *

# Register your models here.




class BookAdmin(admin.ModelAdmin):
    list_display=[field.name for field in Book._meta.fields]
    
admin.site.register(Book, BookAdmin)
