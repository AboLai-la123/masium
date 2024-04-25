from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls',namespace="Home")),
    path('authentication/',include('authentication.urls',namespace="Authentication")),
    path('cars/',include('cars.urls',namespace="Cars")),
    path('products/',include('products.urls',namespace="Products")),
    path('chat/',include('chat.urls',namespace="Chat")),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
