from django.contrib import admin

from .models import Project, Pictures


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'status', 'created_at')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title', 'author', 'status')
    list_filter = ('author', 'status')
    list_per_page = 10
    list_editable = ('status',)
    ordering = ('-id', '-created_at')
    prepopulated_fields = {
        'slug': ('title',),
    }


@admin.register(Pictures)
class PicturesAdmin(admin.ModelAdmin):
    list_display = ('id', 'project')
