from jogador import Jogador
from carta import Carta
import random

# 	Mesa: estado_partida
# 0 - estado inicial local
# 1 - estado_inicial remoto
# 2 - seu turno, jogo em andamento e aguardando jogada a ser selecionada (fatiar/trocar missão/comprar carta/completar missão)
# 3 - turno do oponente, jogo em andamento - aguardando jogada
# 4 - vitória
# 5 - derrota
# 6 - recebeu desistência/abandono, atribui jogador local como vencedor

class Mesa:
    def __init__(self):
        super().__init__()

        self.local_player = Jogador()
        self.remote_player = Jogador()
        self.estado_partida = 0



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
        carta = None
        if num <= 4:
            carta = Carta('src/images/missao1-2.png', 4)       
        elif(num>4 and num <=8):
            carta = Carta('src/images/missao1-4.png', 2)
        elif(num>8):
            carta = Carta('src/images/missao1-8.png', 1)
        print(carta.cardimage)
        return carta
   
    def get_remote_missao(self):
        return self.remote_player.missao
    
    def get_remote_pizza(self):
        return self.remote_player.pizzas
    
    def get_remote_cartas(self):
        return self.remote_player.cartas
    
    def get_remote_area_entrega(self):
        return self.remote_player.area_entrega

    def get_remoteplayer_info(self):
        return [self.remote_player.cartas, self.remote_player.pizzas, self.remote_player.area_entrega, self.remote_player.missao]
    
    def get_localplayer_info(self):
        return [self.local_player.cartas, self.local_player.pizzas, self.local_player.area_entrega, self.local_player.missao]
    
    def fatiar_pizza(self, cardnum):
        carta_jogada = self.local_player.cartas[int(cardnum)]
        if self.local_player.pizzas < carta_jogada.valor:
            return "Pizzas insuficientes para realizar ação"
        else:
            self.local_player.pizzas = self.local_player.pizzas - carta_jogada.valor
            self.local_player.area_entrega = self.local_player.area_entrega + carta_jogada.valor
            self.local_player.cartas.pop(int(cardnum))
            self.estado_partida = 3
            return None
    
    def comprar_carta(self):
        if len(self.local_player.cartas) < 5:  
            self.local_player.cartas.append(self.rand_carta())
            self.estado_partida = 3
            return None
        else:
            return "Limite de cartas atingido"

    def completar_missao(self):
        if self.local_player.missao.valor <= self.local_player.area_entrega:
            self.local_player.area_entrega = self.local_player.area_entrega - self.local_player.missao.valor
            self.local_player.missao = self.rand_missao()
            if self.local_player.area_entrega == 0 and self.local_player.pizzas == 0:
                message = "Vitória"
                self.estado_partida = 4
            else:
                message = "Entrega ok"
                self.estado_partida = 3

            return message
        else:
            return "Não há fatias o suficiente na área de entrega para completar a missão."

    def trocar_missao(self):
        if len(self.local_player.cartas)==5:
            self.local_player.cartas = []
            self.local_player.missao = self.rand_missao()
            self.estado_partida = 3
            return None
        else:
            return "Não há cartas o suficiente para realizar a troca"
    
    def start_match(self):
        local_cartas = self.rand_cartas()
        local_missao = self.rand_missao()
        remote_cartas = self.rand_cartas()
        remote_missao = self.rand_missao()
        self.local_player.inicializar("Green player", 1 , "Green player", local_cartas, local_missao)
        self.remote_player.inicializar("Red player", 2, "Red player", remote_cartas, remote_missao)
        print("Inicializou")

    def receive_start(self):
        print("Entrou no receive_start")
        self.estado_partida = 1

    def receive_move(self, a_move):
        print("Entrou no receive_move")
        print("Estado partida: " + str(self.estado_partida))
        if self.estado_partida == 1:
            #fazer inicializações com o a_move recebido
            print("Entrou no receive move inicial")
            print
            self.remote_player.cartas.append(self.montar_carta_object(a_move['carta0_A']))
            self.remote_player.cartas.append(self.montar_carta_object(a_move['carta1_A']))
            self.remote_player.cartas.append(self.montar_carta_object(a_move['carta2_A']))
            self.remote_player.cartas.append(self.montar_carta_object(a_move['carta3_A']))
            self.remote_player.cartas.append(self.montar_carta_object(a_move['carta4_A']))

            self.local_player.cartas.append(self.montar_carta_object(a_move['carta0_B']))
            self.local_player.cartas.append(self.montar_carta_object(a_move['carta1_B']))
            self.local_player.cartas.append(self.montar_carta_object(a_move['carta2_B']))
            self.local_player.cartas.append(self.montar_carta_object(a_move['carta3_B']))
            self.local_player.cartas.append(self.montar_carta_object(a_move['carta4_B']))

            self.remote_player.pizzas = int(a_move['pizzas_A'])
            self.local_player.pizzas = int(a_move['pizzas_B'])

            self.remote_player.area_entrega = int(a_move['area_entrega_A'])
            self.local_player.area_entrega = int(a_move['area_entrega_B'])

            self.remote_player.missao = self.montar_carta_missao(a_move['missao_A'])
            self.local_player.missao = self.montar_carta_missao(a_move['missao_B'])
            self.estado_partida=3


        elif self.estado_partida == 3:
            print("Entrou no Tratamento de Jogadas")
            #tratamento de jogadas
            card_filename = []
            for count in range(0,5):
                if a_move.get(str(count)) is not None:
                    card_filename.append(a_move.get(str(count)))
            print(card_filename)
            self.remote_player.cartas = []
            for cardname in card_filename:
                self.remote_player.cartas.append(self.montar_carta_object(cardname))
            self.remote_player.pizzas = int(a_move['pizzas'])
            self.remote_player.area_entrega = int(a_move['area_entrega'])
            self.remote_player.missao = self.montar_carta_missao(a_move['missao'])

            print(a_move)
            #libera jogador local p/ jogar
            self.estado_partida=2

    
    def get_estado_partida(self):
        return self.estado_partida
    
    def montar_carta_object(self, txt):
        if txt == 'src/images/fracao1-2.png':
            return Carta('src/images/fracao1-2.png', 4)
        elif txt == 'src/images/fracao1-4.png':
            return Carta('src/images/fracao1-4.png', 2)
        elif txt == 'src/images/fracao1-8.png':
            return Carta('src/images/fracao1-8.png', 1)
    
    def montar_carta_missao(self, txt):
        if txt == 'src/images/missao1-2.png':
            return Carta('src/images/missao1-2.png', 4)
        elif txt == 'src/images/missao1-4.png':
            return Carta('src/images/missao1-4.png', 2)
        elif txt == 'src/images/missao1-8.png':
            return Carta('src/images/missao1-8.png', 1)