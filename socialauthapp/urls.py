
from django.contrib.auth.decorators import login_required
from django.conf.urls import patterns, url
from django.utils.translation import ugettext_lazy as _
from .views import UserUpdateView
from django.contrib.auth import views as auth_views
from socialauthapp.views import addInfoMessage

urlpatterns = patterns('',
    url(r'^update/(?P<pk>[0-9]+)/$', login_required(UserUpdateView.as_view()), 
        name='update_profile'),
)

urlpatterns += patterns('',
    url(r'^login/$', auth_views.login,
        {'template_name': 'fcmsregistration/login.html'},
        name='auth_login'),
    url(r'^logout/$',
        addInfoMessage(auth_views.logout, _('Logged out')),
        {'template_name': 'fcmsregistration/logout.html', },
        name='auth_logout'),
    url(r'^password/change/$',
       addInfoMessage(auth_views.password_change, _('Your password was changed.')),
       {'template_name': 'fcmsregistration/password_change_form.html', },
       name='auth_password_change'),
    url(r'^password/reset/$',
       addInfoMessage(auth_views.password_reset, 
                      _('We\'ve e-mailed you instructions for setting your password\
                       to the e-mail address you submitted. \
                       You should be receiving it shortly.')),
       {'template_name': 'fcmsregistration/password_reset_form.html',
        'email_template_name' : 'fcmsregistration/password_reset_email.html',
        'subject_template_name' : 'fcmsregistration/password_reset_subject.html',
        'post_reset_redirect' : '/'},
       name='auth_password_reset'),
    url(r'^password/reset/confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
       addInfoMessage(auth_views.password_reset_confirm, 
                      _('Your password has been set. \
                       You may go ahead and log in now.')),
       {'template_name': 'fcmsregistration/password_reset_confirm.html',
        'post_reset_redirect' : '/'},
       name='auth_password_reset_confirm'),
    url(r'^password/reset/done/$',
       auth_views.password_reset_done,
       name='auth_password_reset_done')
)