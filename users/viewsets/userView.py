from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from users.serializer.UserSerializer import UserSerializer
from users.models import RegisterUser

class UserView(ViewSet):

    serializer_class = UserSerializer
    Model = User

    # Verificar se o email existe, antes de iniciar o cadastro
    def verifieldUser(self, request):

        email = request.data['email']
        user = User.objects.filter(username=email).exists()

        if(user == True):
            return Response({'mensage': 'email exist', 'status': status.HTTP_409_CONFLICT},
                            status=status.HTTP_409_CONFLICT)
        else:
            return Response({'mensage': 'email approved'}, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):

        ''' Por padrão o django trabalha com
        autenticação com o nome do usuario, porém nos queremos trabalhar com
        email do usuario, quando ele querer logar no sistema.

            Por conta disso ao cadastrar um usuario, invertemos as informações,
        o campo username terá o e-mail do usuario, com isso, conseguimos que
        o login seja feito com o e-mail e não com o nome de usuario. '''
       

        user = User.objects.create_user(
            username=request.data['user']['email'],
            password=request.data['user']['password']
            )

        registerUser = RegisterUser(
            fullName = request.data["fullName"],
             birthDate = request.data["birthDate"],
            male = request.data["male"],
            feminine = request.data["feminine"],
            cpf = request.data["cpf"],
            smartPhone = request.data["smartphone"],
            phone = request.data["phone"],
            user = user
            )
        registerUser.save()

        return Response({'status': "create"}, status=status.HTTP_201_CREATED)
