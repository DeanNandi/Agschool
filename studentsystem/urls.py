from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('studentpage.urls')),
    path('studentpage/', include('studentpage.urls')),
    path('account/', include('account.urls')),
    path('audio/', include('audio.urls')),
    path('files/', include('files.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
