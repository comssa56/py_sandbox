from django.contrib import admin
from django.urls import include, path

from memo.urls import router as memo_router

urlpatterns = [
    path('memo/', include('memo.urls')),
    path('memo/api/', include(memo_router.urls)),
    path('admin/', admin.site.urls),
]