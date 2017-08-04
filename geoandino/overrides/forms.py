# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django import forms
from announcements import forms as announcements_forms
from account import forms as account_forms

class AnnouncementI18nForm(announcements_forms.AnnouncementForm):
    """
    Override original announcements's form for adding translations
    """

    class Meta(announcements_forms.AnnouncementForm.Meta):
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

class SignupCodeI18nForm(account_forms.SignupCodeForm):
    username = forms.CharField(max_length=30, required=False, label=_("Username"))
