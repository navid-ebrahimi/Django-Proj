from django.urls import path, reverse_lazy
from polls import views

app_name = 'app'
urlpatterns = [
    path('horses/', views.HorseListView.as_view(), name='horses'),
    path('horses/<int:pk>', views.HorseDetailView.as_view(), name='horse'),
    path('wacky', views.WackyEquinesView.as_view(), name='whatever'),
    path('', views.ArticleListView.as_view(), name='all'),
    path('article/<int:pk>', views.ArticleDetailView.as_view(), name='article_detail'),
    path('article/create',views.ArticleCreateView.as_view(success_url=reverse_lazy('app:all')), name='article_create'),
    path('article/<int:pk>/update',views.ArticleUpdateView.as_view(success_url=reverse_lazy('app:all')), name='article_update'),
    path('article/<int:pk>/delete',views.ArticleDeleteView.as_view(success_url=reverse_lazy('app:all')), name='article_delete'),
]