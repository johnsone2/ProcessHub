from django.conf.urls import url

from standup.views.views import index

urlpatterns = [
    url(r'^$', index, name='standup_index'),

]