from django.contrib import admin
from .models import *

class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title' , 'datetime' )
    list_display_links = ('id' , 'title')
    list_filter = ('datetime' , )
    search_fields = ('title', 'description' )



# Register your models here.

admin.site.register(Blog, BlogAdmin)