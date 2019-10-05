from django.urls import path, include
from .api.commentsViewSeters import CommenstViewSet

urlpatterns = [
    path("comments", CommenstViewSet.as_view({"get":"list", "post":"create"}), name="comments"),
    path("comments/<int:id_product>", CommenstViewSet.as_view({"get":"productComments"}), name="comentsProducts")
]