'''
Created on Feb 14, 2012

@author: vencax
'''
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages

from .profile import ProfileEditForm

class LoginView(TemplateView):
    template_name = 'registration/login.html'

class UserUpdateView(FormView):
    template_name = 'fcmsregistration/update.html'
    form_class = ProfileEditForm
    
    def get_form_kwargs(self):
        kwargs = super(UserUpdateView, self).get_form_kwargs()
        kwargs['instance'] = self.request.user
        return kwargs
    
    def get_context_data(self, **kwargs):
        ctx = super(UserUpdateView, self).get_context_data(**kwargs)
        ctx['profileform'] = kwargs.pop('form')
        return ctx
    
    def form_valid(self, form):
        form.save()
        messages.info(self.request, _('user details updated'))
        return HttpResponseRedirect('/')

def addInfoMessage(method, info):
    def addInfo(request, **kwargs):
        retval = method(request, **kwargs)
        if isinstance(retval, HttpResponseRedirect):
            messages.info(request, info)
        return retval
    return addInfo