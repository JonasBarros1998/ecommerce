"""
Módulo para envio do link temporario no email do usuario
"""
from django.core.mail import send_mail

class SendEmail():

    def dispatch(self, subject:str, message:str, 
                        email:str, list_email:list, 
                        fail_silently = False):
        """
        `subject`: O assunto do email

        `message`: A mensagem do email

        `email`: O email do usuario

        `list_email`: Tem o tipo`list` contendo uma lista de email, dentro dessa 
        lista voce pode colocar seu prório e-mail

        `fail_silently`: Por padrão ela é False, mas pode ser alterado para True
        """
        send_mail(subject, message, email, list_email, fail_silently = False)

