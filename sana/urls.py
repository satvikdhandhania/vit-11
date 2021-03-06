from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^mds/', include('mds.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    #(r'^admin/', include('admin.site.urls')),
    
    (r'^mds/', 'sana.mds.views.index'),
    (r'^api/', include('sana.api.urls')),
    )
from django.conf import settings
if settings.DEBUG:
    urlpatterns += patterns(
        '',
            
        (r'^contrib/', include('sana.contrib.middleware.urls'),)
)
