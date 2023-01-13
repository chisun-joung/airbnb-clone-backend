from django.contrib import admin
from .models import House

@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    """House admin"""
    list_display = (
        'name', 
        'price_per_night', 
        'address',
        'pets_allowed'
    )
    list_filter = (
        'price_per_night',
        'pets_allowed'
    )
    search_fields = (
        'address',
    )
    fields = (
        'name',
        'address',
        ("price_per_night", "pets_allowed"),
    )
    list_display_links = ("name", "address")
    list_editable = ("price_per_night", "pets_allowed")
    
