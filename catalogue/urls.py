from django.urls import path
from . import views

urlpatterns = [
    path('earrings/', views.earrings_list, name='earrings_list'),
    path('earrings/upload/', views.earring_upload, name='earring_upload'),
    path("earrings/<int:earring_id>/delete/", views.earring_delete, name="earring_delete"),
    
    path('tops/', views.tops_list, name='tops_list'),
    path('tops/upload/', views.top_upload, name='top_upload'),
    path("tops/<int:top_id>/delete/", views.top_delete, name="top_delete"),
    
    path('bottoms/', views.bottoms_list, name='bottoms_list'),
    path('bottoms/upload/', views.bottom_upload, name='bottom_upload'),
    path("bottoms/<int:bottom_id>/delete/", views.bottom_delete, name="bottom_delete"),
    
    path('outfits/', views.outfits_list, name='outfits_list'),
    path('outfits/create/', views.outfit_selection, name='outfit_selection'),
    path('outfits/<int:outfit_id>/', views.outfit_details, name='outfit_details'),
    path("outfits/<int:outfit_id>/delete/", views.outfit_delete, name="outfit_delete"),
    
    path('', views.home, name='home')
]