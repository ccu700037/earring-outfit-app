from django import forms
from .models import Earring, Top, Bottom, Outfit

class EarringForm(forms.ModelForm):
    class Meta:
        model = Earring
        fields = ["name", "image"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": (
                        "w-full px-3 py-2 border border-gray-300 "
                        "rounded-lg focus:outline-none focus:ring-2 "
                        "focus:ring-pink-400"
                    )
                }
            ),
            "image": forms.ClearableFileInput(attrs={"class": "w-full"})
        }
    
class TopForm(forms.ModelForm):
    class Meta:
        model = Top
        fields = ["name", "image"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": (
                        "w-full px-3 py-2 border border-gray-300 "
                        "rounded-lg focus:outline-none focus:ring-2 "
                        "focus:ring-pink-400"
                    )
                }
            ),
            "image": forms.ClearableFileInput(attrs={"class": "w-full"})
        }
        
class BottomForm(forms.ModelForm):
    class Meta:
        model = Bottom
        fields = ["name", "image"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": (
                        "w-full px-3 py-2 border border-gray-300 "
                        "rounded-lg focus:outline-none focus:ring-2 "
                        "focus:ring-pink-400"
                    )
                }
            ),
            "image": forms.ClearableFileInput(attrs={"class": "w-full"})
        }
        
class OutfitForm(forms.ModelForm):
    class Meta:
        model = Outfit
        fields = ["top", "bottom"]