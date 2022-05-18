from django.urls import include, path
from rest_framework import routers

from taco.views import AlimentoViewSet

router = routers.DefaultRouter()

router.register(r'alimentoes', AlimentoViewSet)

urlpatterns = [
    path("", include(router.urls)),
]