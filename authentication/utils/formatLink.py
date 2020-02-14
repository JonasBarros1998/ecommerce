"""
Esse arquivo tem como objetivo retornar um link
completo para o usuario.
"""
def formatLink(baseUrl:str, uri:str, param):
    """
    `baseUrl` A base da url

    `uri` A url que vai ser utilizada
    
    `param` Um parametro que voce deseja adicionar na url, 
    pode ser do tipo int, float ou str
    """
    return f"{baseUrl}/{uri}/{param}"
