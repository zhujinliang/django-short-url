# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.views.generic import RedirectView

from short_url import ShortURL
from short_url.short_url_settings import SHORT_URL_PREFIX


__all__ = [
    'ShortURLRedirectView'
]


class ShortURLRedirectView(RedirectView):
    ''' Redirect short url to long url.'''

    http_method_names = ['get',]
    permanent = False

    def get_redirect_url(self, **kwargs):
        short_url = kwargs.get('short_url', '')
        short_url = short_url.replace(SHORT_URL_PREFIX, '')
        print '=============', short_url
        long_url = reverse('home')
        if short_url:
            url = ShortURL.get_long_url(short_url)
            if url:
                long_url = url
        return long_url

