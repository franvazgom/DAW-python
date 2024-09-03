
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from . import settings
from core.urls import core_urlpatterns
from blog.urls import blog_urlpatterns
from pages.urls import pages_urlpatterns
from services.urls import services_urlpatterns
from contact.urls import contact_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(core_urlpatterns)),
    path('blog/', include(blog_urlpatterns)),
    path('pages/', include(pages_urlpatterns)),
    path('services/', include(services_urlpatterns)),
    path('contact/', include(contact_urlpatterns)),
    re_path(r'^oauth/', include('social_django.urls', namespace='social')),
]

urlpatterns += [
    path("ckeditor5/", include('django_ckeditor_5.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, 
                          document_root=settings.MEDIA_ROOT)