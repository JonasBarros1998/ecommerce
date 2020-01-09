from django.urls import path, include
from .viewSets.createCommentViewSet import CreateCommentViewSet
from .viewSets.commentsSearchViewSet import CommentsSearchViewSet

urlpatterns = [
    path("comments/",
         CreateCommentViewSet.as_view({"post": "create"}), name="new_comments"),
    
    path("comments", CommentsSearchViewSet.as_view(
        {"get": "list"}), name="list_comments"),
    
    path("comments/<int:id_product>",
         CommentsSearchViewSet.as_view(
             {"get": "productComments"}), name="comentsProducts")
]
