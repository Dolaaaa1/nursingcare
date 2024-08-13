from django.urls import path ,include
from .views import *

urlpatterns = [
    
    path("",ListItem.as_view(), name="all_section"),
    path('sections/<int:pk>/',SectionsDetailView.as_view(),name='section_detail'),
    path('success/', SuccessView.as_view(), name='success'),
    path('about-us/', AboutUsView.as_view(), name='about-us'),
    
]

