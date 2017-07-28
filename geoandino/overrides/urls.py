# -*- coding: utf-8 -*-

from django.conf.urls import url, patterns

from .views import CreateAnnouncementI18nView, InviteUserI18nView

# Override geonode's urls with custom views
urlpatterns = patterns(
    "", 
    url(r"^announcements/announcement/create/$", CreateAnnouncementI18nView.as_view(),),
    url(r"^account/invite_user/$", InviteUserI18nView.as_view(),),
)
