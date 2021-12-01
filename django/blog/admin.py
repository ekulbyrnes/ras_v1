from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Page 

# Register your models here.

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'category', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    
class PageAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

admin.site.register(Page, PageAdmin)