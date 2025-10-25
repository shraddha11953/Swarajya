from django.urls import path
from . import views

app_name = 'helpinghand'

urlpatterns = [
    path('', views.home, name='home'), 
    path('submit-offer/', views.submit_offer, name='submit_offer'),
    path('submit-request/', views.submit_request, name='submit_request'),
    path('offers/', views.view_offers, name='view_offers'),
    path('requests/', views.view_requests, name='view_requests'),
    path('my-offers/', views.my_offers, name='my_offers'),
    path('my-requests/', views.my_requests, name='my_requests'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),  # ← NEW
]
