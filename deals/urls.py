from django.urls import path, include
from rest_framework import routers
from .views import FileUploadAPIView

router = routers.DefaultRouter()
router.register(r'deals', FileUploadAPIView, basename="deals")
urlpatterns = router.urls