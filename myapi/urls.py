from django.urls import include, path
from rest_framework import routers
from . import views



router = routers.DefaultRouter()
router.register(r'vehicles', views.VehiclesViewSet, basename='vehicle')
#router.register(r'cars', views.cars , basename='car')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    #path('', include(router.urls)),
    path(r'cars', views.cars),
    path(r'cars/<pk>/', views.carsRemove),
    path(r'rate', views.carsRate),
    path(r'popular', views.carsPopular),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]