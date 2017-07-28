# -*- coding: utf-8 -*-

from announcements import views
from .forms import AnnouncementI18nForm


class CreateAnnouncementI18nView(views.CreateAnnouncementView):
    """
    Override original announcements's create view for adding translations
    """
    form_class = AnnouncementI18nForm
