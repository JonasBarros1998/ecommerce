from .querysetValidate import djangoQuerysetValidate
from rest_framework.response import Response
import json
import sys


class djangoQuerySet:

    def __init__(self):
        self.__djangoQuerysetValidate = djangoQuerysetValidate()

     # Filtrar todos os produtos apartir de um item
    def listFull(self, model, classSerializer: "class serializer", many=True, read_only=False):

        queryset = model.objects.all()
        serializer = classSerializer(
            queryset, many=many, read_only=read_only)
        return serializer.data

    # Filtrar somente um produto, usado para reinderização de detalhes de um produto
    def filterOne(self, ids, model, classSerializer: "class serializer", many=True, read_only=False):

        queryset = model.objects.filter(id=ids)
        serializer = classSerializer(queryset, many=many, read_only=read_only)

        return serializer.data

    # Filtrar por preços
    def filterPrice(self, price, model, classSerializer: "class serializer", many=True, read_only=False):

        price = price.split("ate")
        formatePrice = json.dumps(price)
        listPrice = json.loads(formatePrice)

        lowerPrice = listPrice[0]
        higherPrice = listPrice[1]

        queryset = model.objects.filter(products__price__gte=lowerPrice
                                        ).filter(products__price__lte=higherPrice)

        serializer = classSerializer(queryset, many=many, read_only=read_only)

        return serializer.data

    # Usado para filtragem por marca, modelo ou titulo do produto(usado gerelamente no campo de pesquisa)
    def filterString(self, make, model, classSerializer: "class serializer", many=True, read_only=False, **kwargs):

        try:
            selectFilter = ("make", "model", "title")
            valueFilter = selectFilter.index(make)
        except ValueError:
            self.__djangoQuerysetValidate.checkFilter()

        self.__instance = hasattr(model, "__name__")

        if(self.__instance == False):
            self.__djangoQuerysetValidate.checkInstance(
                'model', self.__instance)

        else:
            if(valueFilter == 0):
                queryset = model.objects.filter(products__make=make)
                serializer = classSerializer(
                    queryset, many=many, read_only=read_only)

            elif(valueFilter == 1):
                queryset = model.objects.filter(products__model=make)
                serializer = classSerializer(
                    queryset, many=many, read_only=read_only)

            elif(valueFilter == 2):
                queryset = model.objects.filter(products__title=make)
                serializer = classSerializer(
                    queryset, many=many, read_only=read_only)

            return serializer.data

    # Filtrar por coluna
    def filterColumn(self, nameColumn, model, classSerializer: "class serializer", repeat=False, many=True, read_only=False):

        if(repeat):
            queryset = model.objects.all().values(nameColumn)
            serializer = classSerializer(
                queryset, many=many, read_only=read_only)
            return serializer.data

        else:
            queryset = model.objects.all().values(nameColumn).distinct(nameColumn)
            serializer = classSerializer(
                queryset, many=many, read_only=read_only)
            return serializer.data

    def querySetSerializer(self, queryset, classSerializer: "class serializer", many=True, read_only=False):

        serializer = classSerializer(queryset, many=many, read_only=read_only)
        return serializer.data
