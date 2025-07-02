from django.contrib import admin
from .models import Top, Bottom, Outfit, Earring, suggest_earrings

@admin.register(Top)
class TopAdmin(admin.ModelAdmin):
    list_display = ("name", "color")

@admin.register(Bottom)   
class BottomAdmin(admin.ModelAdmin):
    list_display = ("name", "color")
   
@admin.register(Outfit)
class OutfitAdmin(admin.ModelAdmin):
    list_display = ("top", "bottom", "created")
    readonly_fields = ("earring_suggestions",)
    
    def earring_suggestions(self, obj):
        earrings = suggest_earrings(obj)
        if not earrings.exists():
            return "No suggestions available"
        return ", ".join([e.name for e in earrings])
    
    earring_suggestions.short_description = "Suggested Earrings"
    
@admin.register(Earring)
class EarringAdmin(admin.ModelAdmin):
    list_display = ("name", "color")
    