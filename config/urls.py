from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    
    url(r'^carts/', include('ecommerce.apps.system.carts.urls')),
    url(r'^products/', include('ecommerce.apps.system.products.urls')),
    url(r'^search/', include('ecommerce.apps.system.search.urls')),
    url(r'^tag/', include('ecommerce.apps.system.tag.urls')),
    url('', include('ecommerce.apps.system.exercise.urls')),
    url(r'^admin/', admin.site.urls),
]


if settings.DEBUG:
    # import debug_toolbar
    
    # urlpatterns = [
    #     path('__debug__/', include(debug_toolbar.urls)),
    #     ]+urlpatterns


    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
