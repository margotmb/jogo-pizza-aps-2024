# valor é definido como quantos 1/8 de pizza a carta vale
# 4 = 4*1/8 = 1/2, metade de uma pizza de 8 pedaços

class Carta:
    def __init__(self, cardimage = None, valor = None):
        self.__cardimage = cardimage
        self.__valor = valor
    
    @property
    def cardimage(self):
        return self.__cardimage

    @property
    def valor(self):
        return self.__valor
