from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from store.views.callback import callback
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
    path('mpesa-callback/', callback, name='callback'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
