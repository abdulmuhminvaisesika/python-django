"""
URL configuration for task_matrimony project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('user_app.urls')),
    path('profiles/', include('user_profile_app.urls')),
    path('preferences/', include('preferance_app.urls')),
    path('maching/', include('maching_app.urls')),
    path('master_table/', include('common_maching_app.urls')),
    path('subcriptions/', include('subcription_app.urls')),
    path('notifications/', include('notification_app.urls')),
    path('messages/', include('message_app.urls')),
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)