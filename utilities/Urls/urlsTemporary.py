import time
import hashlib
import datetime

class Urls():

    def __init__(self):
        self.__hash = None
        self.__secretKey = "'*%2$#!)BgY"
    
    @property
    def hash(self, valueHash)->str:

        generate = self.generateHash()
        self.__hash = generate
        
        if(valueHash == None):
            return self.__hash

        return self.__hash

    def generateHash(self):

        generateCode = hashlib.blake2b(key = self.__secretKey.encode('utf-8'), digest_size = 40)
        return generateCode.hexdigest()

    def defineTime(self):

        timeCurrent = time.strftime('%H:%M')
        return timeCurrent

    def processFinally(self):
        self.hash == None
        return self.hash


