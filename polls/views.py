from django.views import generic
from django.shortcuts import render
from polls.models import Horse, Cat, Article
from polls.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView

# Create your views here.

class HorseListView(generic.ListView):
    model = Horse

class HorseDetailView(generic.DetailView):
    model = Horse

class WackyEquinesView(generic.ListView):
    model = Cat
    template_name = 'polls/wacky.html'

    def get_queryset(self, **kwargs):
        crazy = Horse.objects.all()
        print('CRAZY')
        return crazy

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['crazy_thing'] = 'CRAZY THING'
        return context

class ArticleListView(OwnerListView):
    model = Article
    # By convention:
    # template_name = "polls/article_list.html"


class ArticleDetailView(OwnerDetailView):
    model = Article


class ArticleCreateView(OwnerCreateView):
    model = Article
    fields = ['title', 'text']


class ArticleUpdateView(OwnerUpdateView):
    model = Article
    fields = ['title', 'text']


class ArticleDeleteView(OwnerDeleteView):
    model = Article