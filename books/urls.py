from django.urls import path
from django.conf.urls import url
# from django.contrib.auth.decorators import login_required
# from . import views
# from .models import LikeDislike
# from .models import Article
from .views import BookListView

from . import views

urlpatterns = [
    path('', BookListView.as_view(), name='home'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    url(r'^like/$', views.like_book, name='like'),
]
