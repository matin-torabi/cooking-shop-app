
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static


from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView





# views:

urlpatterns = [
   path('admin/', admin.site.urls),
   path('auth/' , include('authentication.urls')),
   path('profile/' , include('profiles.urls')),
   
   path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
   path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    
    
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


