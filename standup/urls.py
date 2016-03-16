from django.conf.urls import url

from standup.views.views import StandupTaskView

urlpatterns = [
    url(r'^$', StandupTaskView.as_view())
]