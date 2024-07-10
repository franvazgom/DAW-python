from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from core import views
from project import views as views_project

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('project/', views_project.project, name='project'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, 
                          document_root=settings.MEDIA_ROOT)
