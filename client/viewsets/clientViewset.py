from utilities.mongodb.update.update import Update
from utilities.mongodb.insert.insert import Insert
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

class ClientViewset(ModelViewSet):
    def __init__(self):
        self.update = Update()
        self.insert = Insert()
    
    #Atualizar o carrinho do cliente 
    def update_item(self, request):
        find = request.data['find']
        data_update = request.data["datas"]
        response = self.update.find_one_and_update(
            "client", "informations", find, data_update)
        # subistiruir o ObjectId por uma string comum
        response['_id'] = str(response['_id'])

        return Response({"response": response}, status=status.HTTP_200_OK)
    
    #Cria um novo cliente, atribuindo um Id para ele
    def create_client(self, request):
        datas = request.data
        response = self.insert.insert_item("client", "informations", datas)
        response_objectId = str(response.inserted_id)
        return Response({"response": response_objectId}, status=status.HTTP_201_CREATED)
    
    #Pesquise um cliente e atualize o seu endereço
    def find_client_update_address(self, request):
        find = request.data["find"]
        datas = request.data["datas"]
        response = self.update.find_one_and_update("client", "informations", find, datas)
        #substituir um _id por uma string comum 
        response["_id"] = str(response["_id"])
        return Response({"response": response}, status = status.HTTP_200_OK)
    
    #Salvar as compras do clinte: endereço, carrinho e email
    def save_purchase(self, request):
        datas = request.data["datas"]
        find = request.data["find"]
        response = self.update.find_one_and_update("client", "informations", {'id_client': find}, datas)
        #substituir o ObjectId por uma string comum
        response["_id"] = str(response["_id"])
        return Response({"response": response}, status = status.HTTP_201_CREATED)

    
