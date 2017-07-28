# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from announcements import forms, models

class AnnouncementI18nForm(forms.AnnouncementForm):
    """
    Override original announcements's form for adding translations
    """

    class Meta(forms.AnnouncementForm.Meta):
        labels = {
            'title': _('title'),
            'level': _('level'),
            'content': _('content'),
            'site_wide': _('site wide'),
            'members_only': _('members only'),
            'desmissal_type': _('dissmissal type'),
            'publish_start': _('publish start'),
            'publish_end': _('publish end'),
        }
