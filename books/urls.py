from django.urls import path
from django.conf.urls import url
# from django.contrib.auth.decorators import login_required
# from . import views
# from .models import LikeDislike
# from .models import Article
from .views import BookListView
from .views import UserReactionView

from . import views

# app_name = 'ajax'

urlpatterns = [
    path('', BookListView.as_view(), name='home'),
    url(r'^user_reaction/$', UserReactionView.as_view(), name='user_reaction'),
]
