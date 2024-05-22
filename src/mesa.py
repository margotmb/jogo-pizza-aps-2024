from jogador import Jogador
from carta import Carta
import random

# 	Mesa: estado_partida
# 1 - estado inicial
# 2 - partida finalizada (há vencedor)
# 3 - seu turno, jogo em andamento e aguardando jogada a ser selecionada (fatiar/trocar missão/comprar carta/completar missão)
# 4 - seu turno, jogo em andamento e aguardando condições de execução (caso precise selecionar carta)
# 5 - turno do oponente, jogo em andamento - aguardando jogada
# 6 - recebeu desistência/abandono, atribui jogador local como vencedor

class Mesa:
    def __init__(self):
        super().__init__()

        self.local_player = Jogador()
        self.remote_player = Jogador()

        local_cartas = self.rand_cartas()
        local_missao = self.rand_missao()
        remote_cartas = self.rand_cartas()
        remote_missao = self.rand_missao()
        self.local_player.inicializar("Green player", 1 , "Green player", local_cartas, local_missao)
        self.remote_player.inicializar("Red player", 2, "Red player", remote_cartas, remote_missao)

        self.__estado_partida = 0


    def rand_carta(self):
        carta = None
        num = random.randrange(1, 12, 1)
        if num <= 4:
            carta = Carta('src/images/fracao1-2.png', 4)       
        elif(num>4 and num <=8):
            carta = Carta('src/images/fracao1-4.png', 2)
        elif(num>8):
            carta = Carta('src/images/fracao1-8.png', 1)
        return carta

    def rand_cartas(self):
        cartas = []
        for i in range(0,5):
            cartas.append(self.rand_carta())
        return cartas

    def rand_missao(self):
        num = random.randrange(1, 12, 1)
        if num <= 4:
            carta = Carta('src/images/missao1-2.png', 4)       
        elif(num>4 and num <=8):
            carta = Carta('src/images/missao1-4.png', 2)
        elif(num>8):
            carta = Carta('src/images/missao1-8.png', 1)
        return carta

    def get_status(self):
        return self.__estado_partida


    def get_remote_missao(self):
        return self.remote_player.missao
    
    def get_remote_pizza(self):
        return self.remote_player.pizzas
    
    def get_remote_cartas(self):
        return self.remote_player.cartas
    
    def get_localplayer_info(self):
        return [self.local_player.cartas, self.local_player.pizzas, self.local_player.area_entrega, self.local_player.missao]
    
    def fatiar_pizza(self, cardnum):
        carta_jogada = self.local_player.cartas[int(cardnum)]
        self.local_player.pizzas = self.local_player.pizzas - carta_jogada.valor
        self.local_player.area_entrega = self.local_player.area_entrega + carta_jogada.valor
        self.local_player.cartas.pop(int(cardnum))
    
    def comprar_carta(self):
        if len(self.local_player.cartas) < 5:  
            self.local_player.cartas.append(self.rand_carta())
            return None
        else:
            return "Limite de cartas atingido"

    def completar_missao(self):
        NotImplemented