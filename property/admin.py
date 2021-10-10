from django.contrib import admin

from .models import Flat, Complaint, Owner


class MembershipInline(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ['owner', 'flat']


class AuthorAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'id',)
    readonly_fields = ['created_at']
    list_display = (
        'address',
        'price',
        'new_building',
        'construction_year',
        'town',
        )
    list_editable = ['new_building']
    list_filter = ['new_building', 'rooms_number', 'has_balcony']
    raw_id_fields = ['likes']
    inlines = [
        MembershipInline,
    ]


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ['flat', 'user']


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ['flats']
    inlines = [
        MembershipInline,
    ]
    exclude = ('flats',)


admin.site.register(Flat, AuthorAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)
