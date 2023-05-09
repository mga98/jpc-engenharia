from django.contrib import admin

from .models import Materials


@admin.register(Materials)
class MaterialsAdmin(admin.ModelAdmin):
    list_display = ('id', 'material', 'stocked')
    list_display_links = ('id', 'material')
    search_fields = ('id', 'material', 'stocked')
    list_filter = ('material', 'stocked')
    list_editable = ('stocked',)
    ordering = ('-id',)
