from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from rest_framework import routers

from animals.api import views

router = routers.DefaultRouter()
router.register(r'animals', views.AnimalViewSet)
router.register(r'breeds', views.BreedViewSet)
router.register(r'pets', views.PetViewSet)

urlpatterns = [
    url(r'^$', 'animals.views.home', name='home'),

    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, {'next_page': '/'}, name='logout'),

    url(r'^admin/logout/$', logout, {'next_page': '/'}),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^api/', include(router.urls)),
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework'))
]
