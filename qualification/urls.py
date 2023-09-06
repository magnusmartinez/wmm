from django.urls import path
from qualification import views

urlpatterns = [
    path('reports/', views.report, name='monthly-report-by-course'),
    path('report/', views.view_monthly_report_by_course, name='view-monthly-report-by-course'),
    path('pdf/report/', views.pdf_report, name='pdf-report'),
]
