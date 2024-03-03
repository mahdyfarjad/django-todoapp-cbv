from rest_framework.routers import DefaultRouter
from .views import TaskModelViewSet

app_name = 'api_v1'

router = DefaultRouter()
router.register('task', TaskModelViewSet, basename='task')

urlpatterns = router.urls