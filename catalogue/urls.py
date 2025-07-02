from django.urls import path
from . import views

urlpatterns = [
    path('earrings/', views.earrings_list, name='earrings_list'),
    path('earrings/upload/', views.earring_upload, name='earring_upload'),
    
    path('tops/', views.tops_list, name='tops_list'),
    path('tops/upload/', views.top_upload, name='top_upload'),
    
    path('bottoms/', views.bottoms_list, name='bottoms_list'),
    path('bottoms/upload/', views.bottom_upload, name='bottom_upload'),
    
    path('outfits/', views.outfits_list, name='outfits_list'),
    path('outfits/create/', views.outfit_selection, name='outfit_selection'),
    path('outfits/<int:outfit_id/', views.outfit_detail, name='outfit_detail'),
    
    path('', views.home, name='home')
]