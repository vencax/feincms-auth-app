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

class LoginView(TemplateView):
  template_name = 'registration/login.html'

editableFields = ('username', 'first_name', 'last_name', 'email',)
    
class MyUserChangeForm(forms.ModelForm):
    class Meta(UserChangeForm.Meta):
        model = User
        fields = editableFields

class UserUpdateView(UpdateView):
  template_name = 'registration/update.html'
  model = User
  
  def get_form_class(self):
    return MyUserChangeForm
  
  def form_valid(self, form):
    form.save()
    return HttpResponseRedirect('/')
