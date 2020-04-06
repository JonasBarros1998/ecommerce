from django.urls import path, include
from .viewSets.createCommentViewset import CreateCommentViewset
#from .viewSets.commentsSearchViewSet import CommentsSearchViewSet

urlpatterns = [
    path("create/comment/",
         CreateCommentViewset.as_view({"post": "create"}), name="new_comment"),
    
    #path("comments", CommentsSearchViewSet.as_view(
    #    {"get": "list"}), name="list_comments"),
    
    #path("comments/<int:id_product>",
    #     CommentsSearchViewSet.as_view(
    #         {"get": "productComments"}), name="comentsProducts")
]
