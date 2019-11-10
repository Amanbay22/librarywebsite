from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Book
from django.http import JsonResponse
# import json
# from django.http import HttpResponse
# from django.views import View
# from django.contrib.contenttypes.models import ContentType
# from .models import LikeDislike

class BookListView(ListView):
	model = Book
	template_name = 'books/book_list.html'
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_detail.html', {'book': book})


class UserReactionView(ListView):
    template_name = "books/book_list.html"
    def get(self, request, *args, **kwargs):
        book_id = self.request.GET.get("book_id")
        book = Book.objects.get(id="book_id")
        like = self.request.GET.get("like")
        dislike = self.request.GET.get("dislike")
        if like and (request.user not in book.users_reaction.all()):
            book.likes += 1
            book.users_reaction.add(request.user)
            book.save()
        if dislike and (request.user not in book.users_reaction.all()):
            book.dislikes += 1
            book.users_reaction.add(request.user)
            book.save()
        data = {
            'likes': book.likes,
            'dislikes': book.dislikes
        }
        return JsonResponse(data)




# class VotesView(View):
#     model = None  # Модель данных - Статьи или Комментарии
#     vote_type = None  # Тип комментария Like/Dislike
#
#     def post(self, request, pk):
#         obj = self.model.objects.get(pk=pk)
#         # GenericForeignKey не поддерживает метод get_or_create
#         try:
#             likedislike = LikeDislike.objects.get(content_type=ContentType.objects.get_for_model(obj), object_id=obj.id,
#                                                   user=request.user)
#             if likedislike.vote is not self.vote_type:
#                 likedislike.vote = self.vote_type
#                 likedislike.save(update_fields=['vote'])
#                 result = True
#             else:
#                 likedislike.delete()
#                 result = False
#         except LikeDislike.DoesNotExist:
#             obj.votes.create(user=request.user, vote=self.vote_type)
#             result = True
#
#         return HttpResponse(
#             json.dumps({
#                 "result": result,
#                 "like_count": obj.votes.likes().count(),
#                 "dislike_count": obj.votes.dislikes().count(),
#                 "sum_rating": obj.votes.sum_rating()
#             }),
#             content_type="application/json"
#         )
