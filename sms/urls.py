from django.contrib import admin
from django.urls import path, include
from home.views import home, privacy, terms
from home.views import signup
from django.conf import settings
from django.conf.urls.static import static
from home import views

urlpatterns = [
    path("signup/", signup, name="signup"),
path("", home, name="home"),
path("account/", include("django.contrib.auth.urls")),
    path('admin/', admin.site.urls),
# path("signup/", signup, name="signup"),
path("dashboard/", views.dashboard, name="dashboard"),
path('api/', include('home.urls')),
path('users/', include('django.contrib.auth.urls')),
path('privacy/', privacy, name='privacy'),
path('terms/', terms, name='terms'),
]
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
