from django.urls import path, include

from .views import mashin_hesab


urlpatterns = [
    path('', mashin_hesab),
]
