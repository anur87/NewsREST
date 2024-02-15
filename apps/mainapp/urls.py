from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register('category', views.CategoryViewSet)
router.register('news', views.NewsViewSet)

urlpatterns = router.urls