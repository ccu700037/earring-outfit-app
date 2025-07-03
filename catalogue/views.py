from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Earring, Top, Bottom, Outfit, suggest_earrings
from .forms import EarringForm, TopForm, BottomForm, OutfitForm

def earrings_list(request):
    earrings = Earring.objects.order_by("color", "name")
    return render(request, "catalogue/earrings_list.html", {"earrings": earrings})

def earring_upload(request):
    if request.method == "POST":
        form = EarringForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("earrings_list")
    else:
        form = EarringForm()
    return render(request, "catalogue/earring_upload.html", {"form": form, "item_name": "Earrings"})

@require_POST
def earring_delete(request, earring_id):
    earring = get_object_or_404(Earring, id=earring_id)
    earring.delete()
    return redirect("earrings_list")

def tops_list(request):
    tops = Top.objects.order_by("color", "name")
    return render(request, "catalogue/tops_list.html", {"tops": tops})

def top_upload(request):
    if request.method == "POST":
        form = TopForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("tops_list")
    else:
        form = TopForm()
    return render(request, "catalogue/top_upload.html", {"form": form, "item_name": "Top"})

@require_POST
def top_delete(request, top_id):
    top = get_object_or_404(Top, id=top_id)
    top.delete()
    return redirect("tops_list")

def bottoms_list(request):
    bottoms = Bottom.objects.order_by("color", "name")
    return render(request, "catalogue/bottoms_list.html", {"bottoms": bottoms})

def bottom_upload(request):
    if request.method == "POST":
        form = BottomForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("bottoms_list")
    else:
        form = BottomForm()
    return render(request, "catalogue/bottom_upload.html", {"form": form, "item_name": "Bottoms"})

@require_POST
def bottom_delete(request, bottom_id):
    bottom = get_object_or_404(Bottom, id=bottom_id)
    bottom.delete()
    return redirect("bottoms_list")

def outfits_list(request):
    outfits = Outfit.objects.select_related("top", "bottom").order_by("-created")
    return render(request, "catalogue/outfits_list.html", {"outfits": outfits})

def outfit_selection(request):
    if request.method == "POST":
        form = OutfitForm(request.POST)
        if form.is_valid():
            outfit = form.save()
            return redirect("outfit_details", outfit_id=outfit.id)
    else:
        form = OutfitForm()
    return render(request, "catalogue/outfit_selection.html", {"form": form})

def outfit_details(request, outfit_id):
    outfit = get_object_or_404(Outfit, id=outfit_id)
    suggested_earrings = suggest_earrings(outfit)
    return render(request, "catalogue/outfit_details.html", {"outfit": outfit, "suggested": suggested_earrings})

@require_POST
def outfit_delete(request, outfit_id):
    outfit = get_object_or_404(Outfit, id=outfit_id)
    outfit.delete()
    return redirect("outfits_list")

def home(request):
    return render(request, "catalogue/home.html")
