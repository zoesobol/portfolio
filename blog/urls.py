from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogView.as_view(), name='blog'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post-detail'),

]
