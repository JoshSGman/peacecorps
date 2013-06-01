from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from core.views import MapView

urlpatterns = patterns('',

    url(r'^1/$', MapView.as_view(), name="map_view"),
    # Examples:
    # url(r'^$', 'peacecorps.views.home', name='home'),
    # url(r'^peacecorps/', include('peacecorps.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^post/', include('zinnia.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),

#    url(r'^', include('zinnia.urls.capabilities')),
#    url(r'^search/', include('zinnia.urls.search')),
#    url(r'^sitemap/', include('zinnia.urls.sitemap')),
#    url(r'^trackback/', include('zinnia.urls.trackback')),
    url(r'^post/tags/', include('zinnia.urls.tags')),
    url(r'^post/feeds/', include('zinnia.urls.feeds')),
#    url(r'^blog/authors/', include('zinnia.urls.authors')),
#    url(r'^blog/categories/', include('zinnia.urls.categories')),
#    url(r'^blog/', include('zinnia.urls.entries')),
#    url(r'^blog/', include('zinnia.urls.archives')),
#    url(r'^blog/', include('zinnia.urls.shortlink')),
#    url(r'^blog/', include('zinnia.urls.quick_entry')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','data.views.home',name='home'),
    url(r'^register/$', 'data.views.register', name="register")
)
