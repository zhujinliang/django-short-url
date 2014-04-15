# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *

from short_url.views import ShortURLRedirectView


urlpatterns = patterns('',
	url(r'(?P<short_url>[a-z0-9A-Z]{5}$)', ShortURLRedirectView.as_view()),
)
