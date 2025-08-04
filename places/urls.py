from django.urls import path
from .views import nominatim_search

urlpatterns = [
    path('nominatim-test/', nominatim_search, name='nominatim_test'),
]
