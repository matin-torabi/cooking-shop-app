
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static


from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView





# views:

urlpatterns = [
   path('admin/', admin.site.urls),
   # auth:
      path('auth/' , include('authentication.urls')),
   # profile:
      path('profile/' , include('profiles.urls')),
   # product:
      path('product/' , include('products.urls')),
   # admin panel:
      path('panel/' , include('panel.urls')),
   
   # api documents:
   path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
   path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    
    
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


