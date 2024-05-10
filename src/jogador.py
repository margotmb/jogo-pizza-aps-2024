class Jogador:
    def __init__(self):
        self.__identifier = None
        self.__nome = None
        self.__num_jogador = None
        self.__missao = None
        self.__cartas_fracao = []
        self.__pizzas = 16
        self.__meu_turno = False
        self.__vencedor = False

    def inicializar(self, a_number, an_id, a_name):
        self.reset()
        self.__num_jogador = a_number  # int
        self.__identifier = an_id  #   string
        self.__name = a_name  #   string

    def reset(self):
        self.__identifier = None
        self.__nome = None
        self.__num_jogador = None
        self.__missao = None
        self.__cartas_fracao = []
        self.__pizzas = 16
        self.__meu_turno = False
        self.__vencedor = False