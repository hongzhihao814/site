from ..models import News
from django import template

register = template.Library()


@register.simple_tag
def get_news():
    result = News.objects.filter(tag__name='新闻')
    if len(result) > 3:
        return result[:3]
    else:
        return result


@register.simple_tag
def get_notice():
    result = News.objects.filter(tag__name='公告')
    if len(result) >= 1:
        return result[0]
    else:
        return None
