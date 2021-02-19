from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('resume/', views.resume, name='resume'),
    path('portfolio-details/', views.portfolio_details, name='portfolio-details'),
    #path('portfolio/<str:portf>', views.portfolio_details, name='portfolio-details'),
]
