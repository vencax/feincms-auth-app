'''
Created on Jun 18, 2012

@author: vencax
'''
from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class MyUserChangeForm(forms.ModelForm):
    class Meta(UserChangeForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)

class ProfileEditForm(object):
    _forms = set()
        
    @classmethod
    def register_form(self, form):
        self._forms.add(form)
        
    def __init__(self, **kwargs):
        self._instances = []
        self._addInstance(MyUserChangeForm, **kwargs)
        for fClass in self._forms:
            self._addInstance(fClass, **kwargs)
            
    def _addInstance(self, fClass, **kwargs):
        rec = (fClass._meta.model._meta.verbose_name, 
               fClass(**dict(kwargs)))
        self._instances.append(rec)
        
    def get_forms(self):
        return self._instances
    
    def is_valid(self):
        valid = True
        for _, f in self._instances:
            fval = f.is_valid()
            if valid and not fval:
                valid = False
        return valid
    
    def save(self):
        for _, f in self._instances:
            f.save()