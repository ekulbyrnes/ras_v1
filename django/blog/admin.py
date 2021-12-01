from django.contrib import admin
from .models import Page 

# Register your models here.

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'category', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    
admin.site.register(Page, PageAdmin)