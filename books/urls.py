from django.urls import include, path

from .views import BookListView

from . import views

urlpatterns = [
    path('', BookListView.as_view(), name='home'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    path(r'^like/$', views.like_book, name='like'),
]
