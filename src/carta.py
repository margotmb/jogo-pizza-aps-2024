class Carta:
    def __init__(self, cardimage: str, valor: int):
        self.__cardimage = cardimage
        self.__valor = valor
    
    @property
    def cardimage(self):
        return self.__cardimage

    @property
    def valor(self):
        return self.__valor
