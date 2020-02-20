"""
Essa classe tem como principal objetivo saber se o link ainda é valido
O calculo é feito com base de 24 horas, caso a data atual em que foi criada a 
url,  ter um prazo de 24 horas maior que a data de expiração, esse link
já não é mais valido.
"""
from datetime import datetime, date
from rest_framework import status

class DateTime:
    def __init__(self, _datetime):
        self._datetime = datetime.fromisoformat(str(_datetime))
        self._sumDateCurrent = datetime.now()
    
    #metodo para calcular a data
    def calculateDate(self):
        date = self._datetime.fromisoformat(str(self._datetime))
        #Soma a data de expiração Ex: 14/02/2020 = 2036
        sumDateExpire = int(date.day) + int(date.month) + int(date.year)
        #Faz a soma da data atual Ex: 13/02/2020 = 2035
        sumDateCurrent = int(self._sumDateCurrent.day) + \
            int(self._sumDateCurrent.month) + int(self._sumDateCurrent.year)

        return {
            "sumDateExpire": sumDateExpire,
            "sumDateCurrent": sumDateCurrent
        }
    
    #Metodo para calcular a experação do link
    def expire(self, itemDatetime):
        dates = self.calculateDate()
        hourExpire = datetime.fromisoformat(str(itemDatetime))
        hourCurrent = datetime.now() 

        totalMinuteExpire = hourExpire.hour * 60
        totalMinuteCurrent = hourCurrent.hour * 60
        #Verifica se a soma da data de expiração é igual a data atual
        if(dates['sumDateExpire'] == dates['sumDateCurrent']):
            #Verifica se a hora de expiração é menor ou igual a hora atual
            #Se a condição for verdadeira, siguinifica que o horario estourou. 
                if(totalMinuteCurrent > totalMinuteExpire):
                    return status.HTTP_404_NOT_FOUND

                else:
                    return status.HTTP_202_ACCEPTED
        #Verifica se a soma da data atual é menor que a soma da data de expiração, 
        #Se sim o link ainda é valido e não precisamos calcular o horario
        elif(dates['sumDateCurrent'] < dates['sumDateExpire']):
            return status.HTTP_202_ACCEPTED
        
        #Caso a data for maior que a data de expiração, então o link já não existe mais
        else:
            return status.HTTP_404_NOT_FOUND
