"""inventory_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from user import views as user_view
from django.contrib.auth import views as auth_views
# render images in the url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # activate the admin dashboard
    path('admin/', admin.site.urls),
    # include all the path crated in urls.py folder inside dashboard app  
    path('', include('dashboard.urls')),
    # register is from user app and user_view(is how the view is import). .register(is the name ofthe funtion we are calling into the path).
    path('register/', user_view.register, name='user-register'),
    # Login using .LoginView.asview
    path('', auth_views.LoginView.as_view(template_name='user/login.html'), name='user-login'),
    # Logout using .LogoutView.asview
    path('logout/',auth_views.LogoutView.as_view(template_name='user/logout.html'), name='user-logout' ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)