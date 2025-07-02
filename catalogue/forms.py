from django import forms
from .models import Earring, Top, Bottom, Outfit

class EarringForm(forms.ModelForm):
    class Meta:
        model = Earring
        fields = ["name", "image"]
    
class TopForm(forms.ModelForm):
    class Meta:
        model = Top
        fields = ["name", "image"]
        
class BottomForm(forms.ModelForm):
    class Meta:
        model = Bottom
        fields = ["name", "image"]
        
class OutfitForm(forms.ModelForm):
    class Meta:
        model = Outfit
        fields = ["top", "bottom"]