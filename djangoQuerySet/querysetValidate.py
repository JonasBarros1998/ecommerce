from rest_framework.response import Response

class djangoQuerysetValidate:
    def __init__(self):
        pass

    def checkInstance(self, atributeName, instance):

        assert instance == False, f'''{atributeName} 
        não existe um atributo da classe espeficicando o 
        model. O atributo da classe deve ser nomeado como model.'''