import jogador

class Mesa:
    def __init__(self):
        super().__init__()
        self.local_player = jogador.Jogador()
        self.remote_player = jogador.Jogador()
