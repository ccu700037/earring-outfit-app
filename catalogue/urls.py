from django.urls import path
from . import views

urlpatterns = [
    path('earrings/', views.earring_list, name='earring_list'),
    path('earrings/upload/', views.earring_upload, name='earring_upload'),
    
    path('tops/', views.top_list, name='top_list'),
    path('tops/upload/', views.top_upload, name='top_upload'),
    
    path('bottoms/', views.bottom_list, name='bottom_list'),
    path('bottoms/upload/', views.bottom_upload, name='bottom_upload')
]