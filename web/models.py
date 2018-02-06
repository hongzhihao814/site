from django.urls.base import reverse
from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from easy_thumbnails.fields import ThumbnailerImageField
import datetime


class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = verbose_name = '标签'


class News(models.Model):
    title = models.CharField(max_length=250, verbose_name='文章标题')

    body = RichTextUploadingField(verbose_name='文章内容')
    publish = models.DateTimeField(default=timezone.now, verbose_name='发布时间')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    image = ThumbnailerImageField(upload_to=datetime.datetime.now().strftime('news/%Y/%m/%d'), blank=True,
                                  verbose_name='封面')

    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, verbose_name='标签')

    class Meta:
        verbose_name_plural = verbose_name = '文章'
        ordering = ['-publish', 'title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        if self.tag.name == '公告':
            url = 'web:notice_detail'
        else:
            url = 'web:news_detail'
        return reverse(url, args=(self.publish.year, self.publish.strftime('%m'), self.pk))
