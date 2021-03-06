from django.conf.urls import url
from django.contrib.auth import views as auth_views
from authentication.views import hello_world, redirect_to_standup

urlpatterns = [
    url(r'^login/$', auth_views.login, {'template_name': 'authentication/login.html'}),
    url(r'^logout/$', auth_views.logout_then_login ),
    url(r'^profile/$', redirect_to_standup),
    url(r'^hw/$', hello_world)
]