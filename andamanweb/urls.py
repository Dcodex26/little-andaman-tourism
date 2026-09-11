from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),

    path('butler-bay/', views.butler_bay, name='butler_bay'),

    path('kalapathar/', views.kalapathar, name='kalapathar'),

    path('dalda-plantation/', views.dalda_plantation, name='dalda_plantation'),

    path('white-surf/', views.white_surf, name='white_surf'),

    path('enquiry/', views.enquiry, name='enquiry'),

    path(
        'enquiry-success/',
        views.enquiry_success,
        name='enquiry_success'
    ),
]