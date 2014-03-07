from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cluster_gui.views.home', name='home'),
    # url(r'^cluster_gui/', include('cluster_gui.foo.urls')),
    url(r'^$', include('status.urls')),
    url(r'^status/(?P<node>\w+)', 'status.views.monitor_cluster', name='monitor_cluster'),
    url(r'^backup/', 'backup.views.backup', name='backup'),
    url(r'^backup/success', 'backup.views.success', name='success'),
    # a deplavcer les deux dernieres dans leur package respectifs

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
