
from django.contrib.auth.decorators import login_required
from django.conf.urls import patterns, url
from django.contrib.auth.views import logout
from .views import UserUpdateView, LoginView


urlpatterns = patterns('',
    url(r'^update/(?P<pk>[0-9]+)/$', login_required(UserUpdateView.as_view()), 
        name='update_profile'),
    url(r'^login/$', LoginView.as_view(), name='auth_login'),
    url(r'^logout/$', logout, {'next_page' : '/'}, name='auth_logout'),
)