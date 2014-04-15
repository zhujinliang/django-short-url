# -*- coding: utf-8 -*-

import hashlib

from short_url.models import ShortURLMap

from short_url.short_url_settings import SHORT_URL_PREFIX



CODE_MAP = (
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
    'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
    'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 
    'y', 'z', '0', '1', '2', '3', '4', '5', 
    '6', '7', '8', '9', 'A', 'B', 'C', 'D', 
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 
    'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 
    'U', 'V', 'W', 'X', 'Y', 'Z'
)


class ShortURL(object):
    ''' Generate short url according to long url, and get long url according to
    short url.

    usage:
    * get short url:
        s = ShortURL('/long/url/')
        s.get_short_url()
    * get long url:
        ShortURL.get_long_url('7YbNv')
    '''

    def __init__(self, url):
        self.long_url = url
        self.md = self.get_md5(url)

    def get_md5(self, s=None):
        if not s:
            s = self.long_url
        s = s.encode('utf8') if isinstance(s, unicode) else s 
        m = hashlib.md5(s)
        return m.hexdigest()

    def _get_key_list(self):
        hkeys = []
        md = self.md
        for i in xrange(0, 4):
            n = int(md[i*8:(i+1)*8], 16)
            v = []
            e = 0
            for j in xrange(0, 4):
                x = 0x0000003D & n
                e |= ((0x00000002 & n ) >> 1) << j
                v.insert(0, CODE_MAP[x])
                n = n >> 6
            e |= n << 5
            v.insert(0, CODE_MAP[e & 0x0000003D])
            hkeys.append(''.join(v))
        return hkeys

    def get_short_url(self):
        url = ''
        try:
            surl = ShortURLMap.objects.get(code=self.md)
        except ShortURLMap.DoesNotExist:
            key_list = self._get_key_list()
            for key in key_list:
                surls = ShortURLMap.objects.filter(short_url=key)
                if not surls.exists():
                    ShortURLMap.objects.create(code=self.md, short_url=key,
                                url=self.long_url)
                    url = key
                    break
        else:
            url =  surl.short_url

        return SHORT_URL_PREFIX + url

    @classmethod
    def get_long_url(cls, short_url):
        url = ''
        try:
            surl = ShortURLMap.objects.get(short_url=short_url)
        except ShortURLMap.DoesNotExist:
            pass
        else:
            url = surl.url
        return url
