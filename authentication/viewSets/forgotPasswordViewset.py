import random
import os
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv

from django.core.mail import send_mail

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from ..models import Forgot
from ..utils.sendEmail import SendEmail
from ..utils.checkUsername import CheckUsername
from ..utils.formatLink import formatLink
from ..utils.dateTime import DateTime
from ..utils.updatePassword import update

# Configurar o dotenv para fazer a leitura das propriedade do arquivo .env
load_dotenv()
env_path = Path('.') / '.env'

class ForgotPasswordViewset(ModelViewSet):
    def __init__(self):
        self._checkUsername = CheckUsername()
        self._email = SendEmail()
        self._hashLink = random.getrandbits(80)
        self._baseUrl = os.getenv('BASE_URL')
        self._uri = 'authentication/alterar-senha/hash'
    
    #metodo para salvar o hash do usuario no banco de dados
    def create(self, email):
        dateTimeNow = datetime.now()
        forgotPassword = Forgot(hash_link=self._hashLink,
                                datetime=str(dateTimeNow), username = email)
        forgotPassword.save()
    
    #metodo para enviar um e-mail com o link de troca de senha
    def dispatchEmail(self, request):

        email = request.data['username']

        #Deletar algum hash disponivel no banco
        self.delete_hash(email)

        # Verificar se o usuario existe
        user = self._checkUsername.checkUser(email)
       
        if(user):
            # Função para formatar o link com o token gerado
            message = formatLink(self._baseUrl, self._uri, self._hashLink)
           
            # chama o metodo para salvar o token
            self.create(email)

            subject = "Link de recuperação de e-mail"
            # Enviar o email para o usuario
            self._email.dispatch(subject, message, email, [email])
            return Response({"response": "OK"}, status=status.HTTP_200_OK)

        return Response({"status": 204}, status = status.HTTP_200_OK)

    #Método para trocar a senha do usuario
    def forgotPassword(self, request, hash_link):
        #Fazer a consulta do hash no banco de dados
        forgot = Forgot.objects.filter(hash_link = hash_link)
        
        for itens in forgot: 
            dateTime = DateTime(itens.datetime)

            #Verificar se a url ainda é esta no tempo estimado
            validUrl = dateTime.expire(str(itens.datetime))

            #caso o validUrl for igual a status http 202, então a url ainda é valida
            if(validUrl == 202):

                #Função para renovar a senha do usuario
                update(request.data['username'], request.data['password'])
                id = itens.id
                Forgot.objects.get(id = id).delete()
                return Response({"status": 200}, status = status.HTTP_200_OK)

            #vai cair no else, se a url não foi mais valida
            else:
                return Response({}, status = status.HTTP_404_NOT_FOUND)
        return Response({"status": 204}, status = status.HTTP_204_NO_CONTENT)
    
    #Caso tiver algum hash dentro do banco vai ser apagado
    def delete_hash(self, email):
        Forgot.objects.filter(username = email).delete()