
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings
from core.urls import core_urlpatterns
from blog.urls import blog_urlpatterns
from pages.urls import pages_urlpatterns
from services.urls import services_urlpatterns
from contact.urls import contact_urlpatterns

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),
    path('admin/', admin.site.urls),
    path('', include(core_urlpatterns)),
    path('blog/', include(blog_urlpatterns)),
    path('pages/', include(pages_urlpatterns)),
    path('services/', include(services_urlpatterns)),
    path('contact/', include(contact_urlpatterns)),
]

urlpatterns += [
    path("ckeditor5/", include('django_ckeditor_5.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, 
                          document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'La Recova'
admin.site.index_title = 'Panel de administrador'
admin.site.site_title = 'La Recova'