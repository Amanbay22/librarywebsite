from django.urls import path
from django.conf.urls import url
# from django.contrib.auth.decorators import login_required
# from . import views
# from .models import LikeDislike
# from .models import Article
from .views import BookListView
from .views import UserReactionView

from . import views
app_name = 'ajax'

urlpatterns = [
path('', BookListView.as_view(), name='home'),
path('book/<int:pk>/', views.book_detail, name='book_detail'),
url(r'^user_reaction/$', UserReactionView.as_view(), name='user_reaction'),
# url(r'^article/(?P<pk>\d+)/like/$',
    #     login_required(views.VotesView.as_view(model=Article, vote_type=LikeDislike.LIKE)),
    #     name='article_like'),
    # url(r'^article/(?P<pk>\d+)/dislike/$',
    #     login_required(views.VotesView.as_view(model=Article, vote_type=LikeDislike.DISLIKE)),
    #     name='article_dislike'),
    # url(r'^comment/(?P<pk>\d+)/like/$',
    #     login_required(views.VotesView.as_view(model=Comment, vote_type=LikeDislike.LIKE)),
    #     name='comment_like'),
    # url(r'^comment/(?P<pk>\d+)/dislike/$',
    #     login_required(views.VotesView.as_view(model=Comment, vote_type=LikeDislike.DISLIKE)),
    #     name='comment_dislike'),
]
