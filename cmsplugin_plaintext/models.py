from django.utils.translation import ugettext as _
from django.db import models

from cms.models import CMSPlugin


class CMSCharFieldPlugin(CMSPlugin):
    body = models.CharField(_('body'), max_length=500)

    def __str__(self):
        return self.body

    search_fields = ('body',)


class CMSTextFieldPlugin(CMSPlugin):
    body = models.TextField(_('body'))

    def __str__(self):
        return self.body

    search_fields = ('body',)
