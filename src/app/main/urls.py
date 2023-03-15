from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_url, name='get_url'),
    path('<str>', views.redirect_to_url, name='redirect_to_url'),
]
