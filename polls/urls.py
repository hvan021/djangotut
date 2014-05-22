from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('polls.views',
    # ex: /polls/
    url(r'^$', 'index', name='index'),
    # ex: /polls/5/
    url(r'^(?P<poll_id>\d+)/$', 'detail', name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<poll_id>\d+)/results/$', 'results', name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<poll_id>\d+)/vote/$', 'vote', name='vote'),
)

