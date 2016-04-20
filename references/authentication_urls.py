from django.conf.urls import url
from django.contrib.auth import views as auth_views
from authentication.views import hello_world


urlpatterns = [
    url(r'^login/$', auth_views.login, {'template_name': 'authentication/login.html'}),
    url(r'^logout/$', auth_views.logout_then_login ),
    url(r'^hw/$', hello_world)
]