from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers

from animals.api import views

router = routers.DefaultRouter()
router.register(r'animals', views.AnimalViewSet)
router.register(r'breeds', views.BreedViewSet)
router.register(r'pets', views.PetViewSet)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework'))
]
