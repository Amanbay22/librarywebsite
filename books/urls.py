from django.urls import path
from django.conf.urls import url
# from django.contrib.auth.decorators import login_required
# from . import views
# from .models import LikeDislike
# from .models import Article
from .views import BookListView
from .views import UserReactionView

from . import views

urlpatterns = [
path('', BookListView.as_view(), name='home'),
]
