from django.urls import path
from . import views



app_name = 'corruption'




urlpatterns = [
   # path('report/', views.report_corruption, name='report_corruption'),
    #path('my-reports/', views.my_reports, name='my_reports'),
    path('', views.home, name='index'), 
   # path('corruption/',views.index,name='index'),
    path('submit_report/', views.submit_report, name='submit_report'),
    path('my_reports/', views.my_reports, name='my_reports'),
    path('my/', views.my_reports, name='my_reports'),
    path('all_reports/', views.all_reports_admin, name='all_reports_admin'),


]

