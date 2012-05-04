from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

class UserProfile(models.Model):
#    class Meta:
#        verbose_name = _('event')
#        verbose_name_plural = _('events')
#        ordering = ['-event_begin', '-title']
#        get_latest_by = 'event_begin'
#        permissions = (("change_author", ugettext("Change author")),)
#        unique_together = ("event_begin", "title")

    def __unicode__(self):
        return _('Profile of %s') % self.user

    user = models.ForeignKey(User)
    title = models.CharField(_('title'), max_length=255)

