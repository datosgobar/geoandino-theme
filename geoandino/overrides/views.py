# -*- coding: utf-8 -*-

from announcements import views
from account import views as account_views
from .forms import AnnouncementI18nForm, SignupCodeI18nForm


class CreateAnnouncementI18nView(views.CreateAnnouncementView):
    """
    Override original announcements's create view for adding translations
    """
    form_class = AnnouncementI18nForm

class InviteUserI18nView(account_views.InviteUserView):
    """
    Override original account's invite user form for adding translations
    """
    form_class = SignupCodeI18nForm
