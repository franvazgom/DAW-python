
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings
from core.urls import core_urlpatterns
from blog.urls import blog_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(core_urlpatterns)),
    path('blog/', include(blog_urlpatterns))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, 
                          document_root=settings.MEDIA_ROOT)