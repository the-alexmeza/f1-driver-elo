from django.contrib import admin
from .models import Circuit, Race, Driver


class CircuitAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location')


class DriverAdmin(admin.ModelAdmin):
    list_display = ('id', 'driverRef', 'elo')


class RaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Circuit, CircuitAdmin)
admin.site.register(Driver, DriverAdmin)
admin.site.register(Race, RaceAdmin)
