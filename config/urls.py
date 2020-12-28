from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    
    url('', include('ecommerce.apps.system.carts.urls', namespace='carts')),
    url('', include('ecommerce.apps.system.products.urls', namespace='products')),
    url('', include('ecommerce.apps.system.search.urls', namespace='search')),
    url('', include('ecommerce.apps.system.tag.urls', namespace='tag')),
    url('', include('ecommerce.apps.system.exercise.urls',namespace='exercise')),
    url(r'^admin/', admin.site.urls),
]


#Note : name space make us to avoid the same name conflict  in apps 
# dont forget to specify the  app_name="products", in each application with its own name 

if settings.DEBUG:
    # import debug_toolbar
    
    # urlpatterns = [
    #     path('__debug__/', include(debug_toolbar.urls)),
    #     ]+urlpatterns


    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
