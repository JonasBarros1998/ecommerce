#from rest_framework.serializers import ModelSerializer
#from ..models import Comments

comment = ['user', 'date', 'comment']

request = {"user": "jonas", "date": "27/01/1998", "comment": "Bom!!"}

def validate_fields(func):
    def decorator(request, **kwargs):
        print(kwargs['fields'])
        func(request, **kwargs)
    return decorator

@validate_fields
def texto(request, fields):
    return ""

texto(request, fields = comment)