from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import News, Tag


def about(request):
    return render(request, 'web/about.html', {'column': '关于我们', 'about': ' active'})


def branches(request):
    return render(request, 'web/branches.html', {'column': '网点分布', 'branches': ' active'})


def home(request):
    return render(request, 'web/home.html', {'home': ' active'})


def service(request, id=''):
    return render(request, 'web/service.html', {'column': '产品业务', 'service': ' active'})


class NewsListView(ListView):
    tag = ''
    model = News
    template_name = 'web/article_list.html'
    context_object_name = 'articles'
    paginate_by = 8

    def get_queryset(self):
        return super(NewsListView, self).get_queryset().filter(tag__name=self.tag)

    def get_context_data(self, **kwargs):
        context = super(NewsListView, self).get_context_data(**kwargs)
        paginator = context.get('paginator')
        page = context.get('page_obj')
        is_paginated = context.get('is_paginated')
        pagination_data = self.paginate(paginator, page, is_paginated)
        d = {
            'column': '大地新闻',
            'tag': self.tag,
            'news': ' active',
        }
        context.update(d)
        context.update(pagination_data)
        return context

    def paginate(self, paginator, page, is_paginated):
        if not is_paginated:
            return {}

        first = False
        left_more = False
        left = 0
        right_more = False
        right = 0
        last = False
        number = page.number
        total_pages = paginator.num_pages

        if page.has_previous():
            if (number - 2) >= 3:
                first = True
                left_more = True
                left = range(number - 2, number)
            else:
                left = range(1, number)

        if page.has_next():
            if (number + 3) < total_pages:
                last = True
                right_more = True
                right = range(number + 1, number + 3)
            else:
                right = range(number + 1, total_pages + 1)

        pagination_data = {
            'first': first,
            'left_more': left_more,
            'left': left,
            'right_more': right_more,
            'right': right,
            'last': last,
        }

        return pagination_data


class NewsDetailView(DetailView):
    tag = ''
    model = News
    template_name = 'web/article_detail.html'
    context_object_name = 'article'

    def get_object(self, queryset=None):
        new = super(NewsDetailView, self).get_object(queryset=None)
        return new

    def get_context_data(self, **kwargs):
        news = super(NewsDetailView, self).get_context_data(**kwargs)
        d = {
            'column': '大地新闻',
            'tag': self.tag,
            'news': ' active',
        }
        news.update(d)
        return news
