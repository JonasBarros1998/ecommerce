from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from utilities.mongodb.validate.fields import validate_fields
from utilities.mongodb.insert.insert import Insert

class CreateCommentViewset(ModelViewSet):

    def __init__(self):
        self.insert = Insert()

    def create(self, request):
        database = 'client'
        collection = 'comments'
        self.validate(request, fields = ['id', 'user', 'date', 'comment'])
        datas = self.insert.insert_item(database, collection, request.data)
        return Response({"id": str(datas.inserted_id)}, status=status.HTTP_201_CREATED)
    
    @validate_fields
    def validate(self, request, fields):
        return

"""
class CreateCommentViewset:

    # No momento não estão sendo utilizados
    # authentication_classes = [OAuth2Authentication, SessionAuthentication]
    # permission_classes = [TokenHasReadWriteScope]
    
        Função para pegar o nome do usuario, realizando 
    uma consulta no banco atraves do ID do usuario, 
    provindo do localStorage do navegador do usuario

    def searchUser(self, userId):
        user = User.objects.get(id=userId)
        first_name = user.first_name
        last_name = user.last_name
        return f'{first_name} {last_name}'

    def create(self, request, *args, **kwargs):
        nameUser = self.searchUser(request.data['user_id'])
        comments = Comments(
            name = nameUser,
            comment = request.data["comment"],
            avaliation = request.data['avaliation'])
        comments.save()

        comments.product.add(request.data["product"])
        return Response({"response": request.data})
        """
