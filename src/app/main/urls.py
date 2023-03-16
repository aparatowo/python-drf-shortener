from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_url),
    path('<str:id>', views.go_to),
]
