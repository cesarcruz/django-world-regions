from django.contrib import admin
from world_regions.models import Region, RegionCountry


class RegionCountriesInline(admin.TabularInline):
    model = RegionCountry


class RegionAdmin(admin.ModelAdmin):
    inlines = [RegionCountriesInline]

admin.site.register(Region, RegionAdmin)
