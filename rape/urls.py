from django.urls import path
from . import views

app_name = 'rape'

urlpatterns = [
    path('', views.home, name='home'), 
    path('submit/', views.submit_rape_report, name='submit_rape_report'),
    path('my/', views.my_rape_reports, name='my_rape_reports'),
    path('all/', views.all_rape_reports_admin, name='all_rape_reports'),
]
