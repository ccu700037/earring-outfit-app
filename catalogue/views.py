from django.shortcuts import render, redirect
from .models import Earring, Top, Bottom
from .forms import EarringForm, TopForm, BottomForm

def earrings_list(request):
    earrings = Earring.objects.all()
    return render(request, "catalogue/earring_list.html", {"earrings": earrings})

def earring_upload(request):
    if request.method == "POST":
        form = EarringForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("earring_list")
    else:
        form = EarringForm()
    return render(request, "catalogue/earring_upload.html", {"form": form})

def tops_list(request):
    tops = Top.objects.all()
    return render(request, "catalogue/top_list.html", {"tops": tops})

def top_upload(request):
    if request.method == "POST":
        form = TopForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("top_list")
    else:
        form = TopForm()
    return render(request, "catalogue/top_upload.html", {"form": form})

def bottoms_list(request):
    bottoms = Bottom.objects.all()
    return render(request, "catalogue/bottom_list.html", {"bottoms": bottoms})

def bottom_upload(request):
    if request.method == "POST":
        form = BottomForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("bottom_list")
    else:
        form = BottomForm()
    return render(request, "catalogue/bottom_upload.html", {"form": form})