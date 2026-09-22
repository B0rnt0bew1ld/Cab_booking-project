from django.contrib import admin
from .models import Cabs, Station, Passanger

class CabsAdmin(admin.ModelAdmin):
    list_display = ("id", "pick", "drop", "cost")

class PassangerAdmin(admin.ModelAdmin):
    filter_horizontal = ('cabs',)


admin.site.register(Station)
admin.site.register(Cabs, CabsAdmin)
admin.site.register(Passanger, PassangerAdmin)