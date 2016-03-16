from django.conf.urls import url

from standup.views.views import index, StandupTaskView

urlpatterns = [
    url(r'jira/', StandupTaskView.as_view()),
    url(r'^$', index, name='standup_index'),

]