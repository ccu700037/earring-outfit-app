from django.db import models
from PIL import Image
from collections import Counter
import colorsys
import numpy as np
from math import atan2, degrees

class Earring(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="earring/")
    color = models.CharField(max_length=20, blank=True)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        if self.image and not self.color:
            self.color = extract_dominant_color(self.image.path, sat=0.05)
            super().save(update_fields=["color"])
            
    def __str__(self):
        return self.name
    
    
class ClothingBase(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="clothes/")
    color = models.CharField(max_length=20, blank=True)
    added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        abstract = True # don't want a table for ClothingBase
        ordering = ["name"]
        
        
class Top(ClothingBase):
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        if self.image and not self.color:
            self.color = extract_dominant_color(self.image)
            super().save(update_fields=["color"])
            
    def __str__(self):
        return self.name


class Bottom(ClothingBase):
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        if self.image and not self.color:
            self.color = extract_dominant_color(self.image)
            super().save(update_fields=["color"])
            
    def __str__(self):
        return self.name


class Outfit(models.Model):
    top = models.ForeignKey(Top, on_delete=models.CASCADE) # if a top is deleted, delete all outfits based on it
    bottom = models.ForeignKey(Bottom, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.top.name} + {self.bottom.name}"

HUE_LABELS = {
    # split red across the wrap-around
    "red1"  : (  0,  15),
    "pink1" : ( 10,  25),
    "orange": ( 15,  45),
    "yellow": ( 45,  75),
    "green" : ( 75, 165),
    "cyan"  : (165, 195),
    "blue"  : (195, 255),
    "purple": (255, 285),
    "pink2"  : (285, 345),
    "red2"  : (345, 360),
}

def hue_to_name(hue_deg: float) -> str:
    for name, (lo, hi) in HUE_LABELS.items():
        if lo <= hue_deg < hi:
            if name.startswith("red"):
                return "red"
            if name.startswith("pink"):
                return "pink"
            return name
    # shouldn’t get here, but be safe:
    return "red"

    
def extract_dominant_color(path, sat=0.25, val=0.8):
    # ignores desaturated background pixels
    img = Image.open(path).convert("RGB").resize((160, 160))
    img = img.crop((32, 32, 128, 128))
    arr = np.asarray(img) / 255.0 # divide by 255 to normalize. arr is (160, 160, 3)
    r, g, b = arr[..., 0], arr[..., 1], arr[..., 2] # ... notation is all preceding axes in numpy
    
    h, s, v = np.vectorize(colorsys.rgb_to_hsv)(r, g, b)
    global_sat = s.mean()
    if global_sat < 0.07 and v.mean() > 0.5:
        return "gray"
    
    # mask out sat too low or brightness too high
    mask = (s > sat) & (v < val) # boolean array
    if np.count_nonzero(mask) < 50:
        mask = np.ones_like(mask) # filtered too much, keep all
        
    # circular mean 
    hues = (h[mask] * 360).astype(int)
    hist, edges = np.histogram(hues, bins=36, range=(0, 360))

    # ignore bins with very few pixels
    hist[hist < 60] = 0 # min_pixels=200
    if hist.max() == 0:          # all bins too small
        return "gray"


    # peak_bin = hist.argmax()
    hist_smoothed = np.convolve(hist, [1, 1, 1], mode="same")
    peak_bin = hist_smoothed.argmax()
    dominant_hue = (edges[peak_bin] + edges[peak_bin + 1]) / 2

    print("DEBUG dominant_hue:", dominant_hue)

    
    mean_sat = s[mask].mean()
    mean_val = v[mask].mean()
    if mean_val < 0.15:
        return "black"
    elif mean_val > 0.9 and mean_sat < 0.15:
        return "white"
    elif mean_sat < 0.2:
        return "gray"
    else:
        label = hue_to_name(dominant_hue)
        if label == "red" and mean_val > 0.70 and mean_sat < 0.50:
            label = "pink"
        return label
    
EARRING_PALETTE = {
    "red":    ["yellow", "white", "black", "red"],
    "orange": ["yellow", "blue", "orange"],
    "yellow": ["purple", "white", "brown", "yellow"],
    "green":  ["green", "gold", "pink"],
    "blue":   ["blue", "gray", "white", "yellow", "cyan"],
    "purple": ["yellow", "purple"],
    "pink":   ["gray", "white", "pink", "yellow"],
    "brown":  ["cyan", "orange", "yellow"],
    "black":  ["yellow", "gray", "red", "white", "pink", "black"],
    "white":  ["red", "blue", "green", "purple", "yellow", "pink", "black", "white"],
    "gray":   ["gray", "pink", "blue"],
}
    
def suggest_earrings(outfit):
    top_color = outfit.top.color
    bottom_color = outfit.bottom.color
    
    
    neutral_colors = ["white", "gray", "black"]
    
    if top_color not in neutral_colors and bottom_color in neutral_colors:
        matching_colors = EARRING_PALETTE[top_color]
    else:
        matching_colors = EARRING_PALETTE[bottom_color]
        
    return Earring.objects.filter(color__in=matching_colors)