'''
Created on Feb 14, 2012

@author: vencax
'''
from django.http import HttpResponseRedirect
from django.views.generic.edit import UpdateView
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django import forms
from django.views.generic.base import TemplateView
from django.conf import settings
from django.contrib import messages

class LoginView(TemplateView):
    template_name = 'registration/login.html'

editableFields = ('username', 'first_name', 'last_name', 'email',)
    
class MyUserChangeForm(forms.ModelForm):
    class Meta(UserChangeForm.Meta):
        model = User
        fields = editableFields

class UserUpdateView(UpdateView):
    template_name = 'fcmsregistration/update.html'
    model = User
    
    def get_form_class(self):
        return MyUserChangeForm
    
    def get_context_data(self, **kwargs):
        ctx = super(UserUpdateView, self).get_context_data(**kwargs)
        if 'org_member' in settings.INSTALLED_APPS:
            from org_member.views import on_update_view
            ctx.update({'extra_content' : on_update_view(self.request)})
        return ctx
    
    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect('/')

def addInfoMessage(method, info):
    def addInfo(request, **kwargs):
        retval = method(request, **kwargs)
        if isinstance(retval, HttpResponseRedirect):
            messages.info(request, info)
        return retval
    return addInfo