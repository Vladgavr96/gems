from django.urls import path, include
from rest_framework import routers
from .views import FileUploadAPIView, Top5CustomersAPIView

router = routers.DefaultRouter()
router.register(r'upload', FileUploadAPIView, basename="upload"),
router.register(r'top5', Top5CustomersAPIView, basename="top5"),

urlpatterns = router.urls