"""
URL configuration for party_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
# party_project/urls.py
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import include, path
from django.contrib.auth import views as auth_views
from profiles.views import custom_logout  # Import the custom_logout view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('profiles/', include('profiles.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='profiles/login.html'), name='login'),
    path('logout/', custom_logout, name='logout'),  # Use the custom_logout view
    path('quizzes/', include('quizzes.urls')),
    path('gallery/', include ('gallery.urls')),
    path('spinning_wheel/', include('spinning_wheel.urls')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)