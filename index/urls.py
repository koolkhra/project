from django.urls import path ,include
from . import views
urlpatterns = [
    path('login/', views.login,name='login'),
    path('save-location/', views.save_location, name='save_location'),
]
