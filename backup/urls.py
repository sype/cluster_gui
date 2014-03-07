__author__ = 'sype'

from django.conf.urls.defaults import patterns, include, url



urlpatterns = patterns('',
    # Examples:
    url(r'^backup/', 'backup.views.check_stats', name="check_stats"),


    # url(r'^cluster_gui/', include('cluster_gui.foo.urls')),
    #url(r'^cluster_gui/', include(status.urls)),

    # Uncomment the admin/doc line below to enable admin documentation:


    # Uncomment the next line to enable the admin:

)

