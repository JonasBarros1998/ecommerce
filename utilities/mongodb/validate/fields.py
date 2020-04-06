def validate_fields(func):
    def decorator(request, **kwargs):
        field_number(request.data, kwargs["fields"])
        compare_fields(request.data, kwargs["fields"])
        func(request, **kwargs)
    return decorator

#Comparar a quantidade de itens que existe em cada campo
def field_number(data_request, fields):
    keys = data_request.keys()
    count_keys = len(keys)
    count_fields = len(fields)

    if(count_fields == count_keys):
        raise f'''Os campos que vieram da requisição, não tem a mesma quantidade dos
            campos passados como parametro na função'''
    else:
        return True

#Compara se os campos são iguais
def compare_fields(data_request, fields):
    data_keys = data_request.keys()
    for field in fields:
        if(field not in data_keys):
            raise f"O campo ${field} não existe"
    return True
