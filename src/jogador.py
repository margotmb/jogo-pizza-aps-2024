#ver necessidade de identificador -> simplificar

class Jogador:
    def __init__(self):
        self.__identificador = None
        self.__nome = None
        self.__num_jogador = None
        self.__missao = None
        self.__cartas = []
        self.__pizzas = 16
        self.__area_entrega = 0
        self.__vencedor = False

    def inicializar(self, an_id, a_number, a_name, cartas_fracao: list, missao ):
        self.reset()
        self.__identificador = an_id  #   string
        self.__nome = a_name  #   string
        self.__num_jogador = a_number  # int
        self.__cartas = cartas_fracao
        self.__missao = missao

    def reset(self):
        self.__identificador = None
        self.__nome = None
        self.__num_jogador = None
        self.__missao = None
        self.__cartas = []
        self.__pizzas = 16
        self.__area_entrega = 0
        self.__vencedor = False

    @property
    def missao(self):
        return self.__missao
    
    @missao.setter
    def missao(self, nova_missao):
        self.__missao = nova_missao

    @property
    def cartas(self):
        return self.__cartas
    
    @cartas.setter
    def cartas(self, new_cartas):
        self.__cartas = new_cartas

    @property
    def pizzas(self):
        return self.__pizzas
    
    @pizzas.setter
    def pizzas(self, new_pizza_value):
        self.__pizzas = new_pizza_value
    
    @property
    def area_entrega(self):
        return self.__area_entrega
    
    @area_entrega.setter
    def area_entrega(self, new_value):
        self.__area_entrega = new_value