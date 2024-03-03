from rest_framework.routers import DefaultRouter
from .views import TaskModelViewSet

router = DefaultRouter()
router.register('task', TaskModelViewSet, basename='task')

urlpatterns = router.urls