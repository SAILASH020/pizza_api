from rest_framework import routers
from .views import piza_viewset

router = routers.DefaultRouter()
router.register('pizza', piza_viewset)