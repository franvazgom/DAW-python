from rest_framework import routers
from django.urls import path, include
from projects.api import ProjectViewSet
from projects.api_g import DataTest

router = routers.DefaultRouter()
router.register('api/projects', ProjectViewSet, 'projects')

# urlpatterns = router.urls

urlpatterns = [
    path('api/projects/', include(router.urls)),
    path('dataTest/', DataTest.as_view()),
]

