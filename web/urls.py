from django.conf.urls import url
from django.conf.urls.static import static
from ddvb import settings
from . import views

app_name = 'web'
urlpatterns = [
                  url(r'^$', views.home, name='home'),
                  url(r'^news/$', views.NewsListView.as_view(tag='新闻'), name='news'),
                  url(r'^notice/$', views.NewsListView.as_view(tag='公告'), name='notice'),
                  url(r'^news/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/(?P<pk>[0-9]+)/$',
                      views.NewsDetailView.as_view(tag='新闻'), name='news_detail'),
                  url(r'^notice/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/(?P<pk>[0-9]+)/$',
                      views.NewsDetailView.as_view(tag='公告'), name='notice_detail'),
                  url(r'^service/(?P<id>[\w-]*)$', views.service, name='service'),
                  url(r'^branches/$', views.branches, name='branches'),
                  url(r'^about/$', views.about, name='about'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
