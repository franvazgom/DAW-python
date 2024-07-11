
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from core import views as views_core

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views_core.home, name='home'),
    path('about/', views_core.about, name='about'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, 
                          document_root=settings.MEDIA_ROOT)