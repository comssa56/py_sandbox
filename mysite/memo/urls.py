from django.urls import path
from . import views

from rest_framework import routers
from .views import MemoViewSet

router = routers.DefaultRouter()
router.register(r'memos', MemoViewSet)

urlpatterns = [
    path('', views.index, name='index'),
]
