from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('about-delivery/', views.AboutDeliveryView.as_view(), name='about_delivery'),
    path('contacts/', views.ContactView.as_view(), name='contacts')
]