from django.contrib import admin

from .models import Flat, Complaint


class AuthorAdmin(admin.ModelAdmin):
    search_fields = ('owner', 'town', 'address', )
    readonly_fields = ['created_at']
    list_display = (
        'address',
        'price',
        'new_building',
        'owners_phonenumber',
        'owner_pure_phone',
        'construction_year',
        'town',
        )
    list_editable = ['new_building']
    list_filter = ['new_building', 'rooms_number', 'has_balcony']
    raw_id_fields = ['likes']


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ['flat', 'user']


admin.site.register(Flat, AuthorAdmin)
admin.site.register(Complaint, ComplaintAdmin)
