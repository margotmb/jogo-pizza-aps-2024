import jogador
import carta

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

        # Instancia jogadores e os define
        self.local_player = jogador.Jogador()
        self.remote_player = jogador.Jogador()
        self.local_player.inicializar(1, "Green player", "Green player")
        self.remote_player.inicializar(2, "Red player", "Red player")
        self.__baralho_fracoes  = []
        self.__baralho_missoes = []
        self.__estado_partida = 1



    def get_status(self):
        return self.__estado_partida