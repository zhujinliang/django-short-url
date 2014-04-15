# -*- coding: utf-8 -*-

from django.db import models


class ShortURLMap(models.Model):
    ''' Record short url map.'''

    code = models.CharField(max_length=60, db_index=True, unique=True,
                verbose_name=u'长url的MD5码')
    short_url = models.CharField(max_length=20, db_index=True,
                verbose_name=u'短url')
    url = models.CharField(max_length=500, verbose_name=u'实际url')
    created_on = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')

    class Meta:
        db_table = 'surl_short_url_map'
        ordering = ['created_on', ]
        verbose_name = u'短链接映射表'
        verbose_name_plural = u'短链接映射表'

    def short_url_link(self):
        from short_url.short_url_settings import SHORT_URL_PREFIX
        url_link = SHORT_URL_PREFIX + self.short_url
        return '<a href="%s" target="_blank">打开短链接</a>' % (url_link)
    short_url_link.allow_tags = True
    short_url_link.short_description = u'短链接'

    def long_url_link(self):
        return '<a href="%s" target="_blank">%s</a>' % (self.url, self.url)
    long_url_link.allow_tags = True
    long_url_link.short_description = u'实际链接'
