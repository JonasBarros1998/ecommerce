"""
Essa classe tem como funcionalidade verificar se o cliente 
passou corretamente os parametros na url
"""
from rest_framework.response import Response

class Params:

    def url_params(self, request):
        verifield_params = self.__verifield_params(request)
        if(verifield_params):
            return verifield_params

    def __verifield_params(self, request):
        page = request.query_params.__contains__('page')
        itens = request.query_params.__contains__('itens')
        if(not page):
            raise print("param page is False")
        elif (not itens):
            raise print(f"param itens is False")
        else:
            return {
                'page': request.query_params['page'],
                'itens': request.query_params['itens']
            }
