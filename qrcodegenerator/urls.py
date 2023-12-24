from django.urls import path

from .views import qr_code_generator

urlpatterns = [
    path("", qr_code_generator.index, name="index"),
]
