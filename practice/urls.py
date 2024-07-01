from django.contrib import admin
from django.urls import path
from crude.views import home, delete_stds, Update_stds

urlpatterns = [
    path('', home, name='home'),
    path('delete_stds/<int:id>/', delete_stds, name='delete_stds'),
    path('update_stds/<int:id>/', Update_stds, name='update_stds'),
    path('admin/', admin.site.urls),
]
