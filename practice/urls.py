from django.contrib import admin
from django.urls import path
from crude.views import home, delete_stds, Update_stds
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('', home, name='home'),
    path('delete_stds/<int:id>/', delete_stds, name='delete_stds'),
    path('update_stds/<int:id>/', Update_stds, name='update_stds'),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()