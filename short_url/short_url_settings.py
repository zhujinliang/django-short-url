# -*- coding: utf-8 -*-

from django.conf import settings

SHORT_URL_PREFIX = getattr(settings, 'SHORT_URL_PREFIX', '/s/')
