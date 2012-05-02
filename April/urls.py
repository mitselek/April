from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from bubble.models import BubbleDefinition

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$','April.views.index', name='home'),
    url(r'^$',
        ListView.as_view(
            queryset = BubbleDefinition.objects.order_by('label')[:500],
            context_object_name='bubbledefinitions',
            template_name='bubble/index.html')),

    url(r'^bubbledefinition/(?P<bubbledefinition_id>\d+)/$', 'April.views.bubbledefinition'),

    # url(r'^April/', include('April.foo.urls')),

    # url(r'^polls/$', 'polls.views.index'),
    # url(r'^polls/(?P<poll_id>\d+)/$', 'polls.views.detail'),
    # url(r'^polls/(?P<poll_id>\d+)/results/$', 'polls.views.results'),
    # url(r'^polls/(?P<poll_id>\d+)/vote/$', 'polls.views.vote'),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)
