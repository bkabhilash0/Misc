from django.contrib import admin
from .models import Post, Comment

# Register your models here.
class DateAdmin(admin.ModelAdmin):
    readonly_fields = ('date_time','last_updated',)
    list_display = ('name','email','title','date_time','last_updated')
    list_filter = ('date_time','last_updated')
    search_fields = ('email','name','title',)
    raw_id_fields = ('author',)

admin.site.register(Post, DateAdmin)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated',)
    list_display = ('name','email','post','created','active',)
    list_filter = ('active','created','updated')
    search_fields = ('name','email','body')
