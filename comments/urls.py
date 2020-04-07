from django.urls import path, include
from .viewSets.createCommentViewset import CreateCommentViewset
from .viewSets.listingCommentsViewset import ListingCommentsViewset

urlpatterns = [

    # Criar um novo comentario
    path("create/comment/",
         CreateCommentViewset.as_view({"post": "create"}),
         name="create_comment"),

    # Listar todo os comentarios
    path("comments/", ListingCommentsViewset.as_view({"get": "list"}),
         name="list_comments")
]
