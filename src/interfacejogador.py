from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from mesa import Mesa
from dog.dog_interface import DogPlayerInterface
from dog.dog_actor import DogActor
import sys


class InterfaceJogador(DogPlayerInterface):
    def __init__(self):
        # Instanciar Tk
        self.main_window = Tk()
        self.mesa = Mesa()# Tratamento do domínio do problema
        # Organização e preenchimento da janela  
        self.fill_main_window()

        # Set Player Name
        player_name = simpledialog.askstring(title="Player identification", prompt="Qual o seu nome?")

        # Dog 
        self.dog_server_interface = DogActor()
        message = self.dog_server_interface.initialize(player_name, self)
        messagebox.showinfo(message=message)

        text_string = "Olá, " + player_name + "\n\n Clique no botão abaixo para começar"
        self.player_name = Label(self.main_window, text=text_string, bg="khaki1", borderwidth=3, relief="ridge")
        self.player_name.place(width = 300, height=100, anchor='center', relx=0.5, rely=0.4)

        # Main Loop
        self.main_window.mainloop()

    # Popula a janela Tk com os elementos
    def fill_main_window(self):
        estado_partida = self.mesa.get_estado_partida()
        self.main_window.title("Jogo da Pizza")
        #self.main_window.iconbitmap("src/images/icon.ico")
        self.main_window.resizable(False, False)
        self.main_window.geometry("1280x720")

        self.bg_img = PhotoImage(file="src/images/init_bg.png")
        self.bg_label = Label(self.main_window, image = self.bg_img)
        self.bg_label.place(x=0,y=0)
        
        self.start_button = Label(self.main_window, text = "Iniciar Partida", width=100, height=100, borderwidth=2, relief="groove")
        self.start_button.place(width=150, height=50, anchor='center', relx=0.5, rely=0.55)
        self.start_button.bind("<Button-1>", lambda e: self.start_match())
        #self.start_button.bind("<Button-1>", lambda e: self.update_interface(estado_partida))

    def update_interface(self,estado_partida):
        if estado_partida == 0 or estado_partida == 1:
            self.start_button.destroy()
        print(estado_partida)
        #Disposição da Interface: Ver template_interface.png
        #Estado atual: produzindo a interface em sua versão template.
        #Futuramente alterar para receber essas informações através da mesa

        #Frame oponente
        self.frame_oponente = Frame(self.main_window, width=1280, height=250, bg="red")
        self.frame_oponente.grid(row=0, column=0)

        #Label Missao
        remote_missao = self.mesa.get_remote_missao()
        self.img_missao_oponente = PhotoImage(file=remote_missao.cardimage)
        self.missao_oponente = Label(self.frame_oponente, 
                                           bg='red', 
                                           #text="label_missao_oponente",
                                           image=self.img_missao_oponente
                                           )
        self.missao_oponente.place(width=300, height=250, x=0, y=0)
        

        #Label Pizzas
        remote_pizza = self.mesa.get_remote_pizza()
        if remote_pizza >= 10:
            remote_pizza_filename = 'src/images/pizza' + str(remote_pizza) + '.png'
        else:
            remote_pizza_filename = 'src/images/pizza0' + str(remote_pizza) + '.png'

        self.img_pizza_oponente = PhotoImage(file=remote_pizza_filename)
        self.pizza_oponente = Label(self.frame_oponente,
                                          bg='maroon',
                                          image=self.img_pizza_oponente)
        self.pizza_oponente.place(width=400, height=200, x=300, y=0)

        # Area Entrega - Oponente

        area_entrega_oponente = self.mesa.get_remote_area_entrega()
        txt_oponente = "Area Entrega Oponente: " + str(area_entrega_oponente) + " fatias prontas"
        self.area_entrega = Label(self.frame_oponente,
                                  bg='pink',
                                  text=txt_oponente
                                  )
        self.area_entrega.place(width=400, height=50, x=300, y=200)
        
        # -- Frame Cartas Oponente
        self.frame_cartas_oponente = Frame(self.frame_oponente, width=600, height=250, bg="green")
        self.frame_cartas_oponente.place(x=700, y=0)
        self.cartas_oponente = self.mesa.get_remote_cartas()
        
        #Imagens de Carta
        self.imagens_carta_oponente = []
        for carta in self.cartas_oponente:
            self.imagens_carta_oponente.append(PhotoImage(file=carta.cardimage))

        #Labels de Cartas
        self.label_cartas_oponente= [] 
        for imagem_op in self.imagens_carta_oponente:
            a_Label = Label(self.frame_cartas_oponente, image=imagem_op, bg="grey")
            self.label_cartas_oponente.append(a_Label)
        
        #Posiciona as cartas no grid
        col=0
        for label in self.label_cartas_oponente:
            label.grid(row=0, column=col, padx=7, pady=60)
            col = col + 1
        # -- 
        
        # -----
        #Frame central -> Frame Baralhos -> label:baralho_fracoes, label: baralho_missoes
        self.frame_central = Frame(self.main_window, width=1280, height=220, bg="khaki1")
        self.frame_central.grid(row=1, column=0)

        self.baralho_fracoes = Label(self.frame_central, text="Ação: Comprar Carta de Fração", bg='yellow', borderwidth=2, relief="solid")
        self.baralho_fracoes.place(width=300, height=220, x=340, y=0)
        

        self.baralho_missoes = Label(self.frame_central, text="Ação: Trocar missão", bg="green", borderwidth=2, relief="solid")
        self.baralho_missoes.place(width=300, height=220, x=660, y=0)

        text_state = "Estado da Partida: "
        if estado_partida == 2 or estado_partida == 0:
            text_state = text_state + "Aguardando Jogada Local"
        elif estado_partida == 3 or estado_partida == 1:
            text_state = text_state + "Aguardando Jogada Remota"
        self.estado_partida = Label(self.frame_central, text=text_state, bg='white', borderwidth=1, relief='solid', padx=-10, pady=-10)
        self.estado_partida.place(width=339, height=50, x = 0, y = 0)

        # ----

        #Frame jogador
        self.frame_jogador = Frame(self.main_window, width=1280, height=250, bg="blue")
        self.frame_jogador.grid(row=2, column=0)

        #Frame Cartas Jogador
        self.frame_cartasjogador = Frame(self.frame_jogador, width=620, height=250, bg='green', padx=5)
        self.frame_cartasjogador.place(x=0, y=0)

        #IMPLEMENTAR -> Solução geral, get_player_info, 0-Cartas, 1-Pizzas, 2- Area de Entrega, 3-Missão
        self.localplayer_info = self.mesa.get_localplayer_info()
        self.cartas_jogador= self.localplayer_info[0]
        
        #Imagens de Carta
        self.imagens_cartajogador = []
        for carta in self.cartas_jogador:
            self.imagens_cartajogador.append(PhotoImage(file=carta.cardimage))

        #Labels de Cartas
        self.label_cartasjogador= [] 
        for imagem in self.imagens_cartajogador:
            a_Label = Label(self.frame_cartasjogador, image=imagem, bg="grey")
            self.label_cartasjogador.append(a_Label)
        
        #Atribui um número para cada carta, no campo text -> Utilizado para identificação ao interagir com a mesa
        cardnum=[0,1,2,3,4]
        for i in range (0, len(self.label_cartasjogador)):
            self.label_cartasjogador[i].config(text=str(cardnum[i]))
        


        #Posiciona as cartas no grid
        col=0
        for label in self.label_cartasjogador:
            label.grid(row=0, column=col, padx=10, pady=60)
            col = col + 1

        # pizza_jogador
        print("self local pizza: " + str(self.localplayer_info[1]))
        local_pizza = self.localplayer_info[1]
        if local_pizza >= 10:
            local_pizza_filename = 'src/images/pizza' + str(local_pizza) + '.png'
        else:
            local_pizza_filename = 'src/images/pizza0' + str(local_pizza) + '.png'
        self.img_pizza_jogador = PhotoImage(file=local_pizza_filename)
        self.pizza_jogador = Label(self.frame_jogador,
                                         bg='navyblue',
                                        image=self.img_pizza_jogador)
        self.pizza_jogador.place(width=400, height=200, x=620, y=50)

        # area entrega -> self.localplayer_info[2]
        area_entrega = self.localplayer_info[2]
        txt = "Area Entrega: " + str(area_entrega) + " fatias prontas"
        self.area_entrega = Label(self.frame_jogador,
                                  bg='pink',
                                  text=txt 
                                  )
        self.area_entrega.place(width=400, height=50, x=620, y=0)


        # missao_jogador
        #self.localplayer_info[3]
        self.local_carta_missao = self.localplayer_info[3]
        local_carta_missao_filename = self.local_carta_missao.cardimage
        self.img_missao_jogador = PhotoImage(file=local_carta_missao_filename)
        self.missao_jogador = Label(self.frame_jogador,
                                          bg="blue",
                                          image=self.img_missao_jogador)
        
        self.missao_jogador.place(width=200, height=250, x=1050, y=0)

        ## Seção Binds de Função -> Só cria caso seja o turno do jogador local##
        if estado_partida == 2 or estado_partida == 0:
            self.baralho_fracoes.bind("<Button-1>", self.comprar_carta)

            #Atribui bind fatiar_pizza às labels
            for a in self.label_cartasjogador:
                a.bind("<Button-1>", self.fatiar_pizza)

            self.missao_jogador.bind("<Button-1>", self.completar_missao)
            self.baralho_missoes.bind("<Button-1>", self.trocar_missao)
        #print(a.cget("text"))

    def fatiar_pizza(self, event):
        #objeto EVENT tem uma referencia ao widget label que está atrelado ao clique
        #print(event.widget.cget("text"))
        num = event.widget.cget("text")
        message = self.mesa.fatiar_pizza(num)
        if message is not None:
            messagebox.showinfo(message=message)
        else:
            self.update_interface(self.mesa.get_estado_partida())
            dict = self.montar_dict()
            dict['match_status'] = "next"
            self.dog_server_interface.send_move(dict)

    def comprar_carta(self, event):
        message = self.mesa.comprar_carta()
        if message is not None:
            messagebox.showinfo(message=message)
        else:
            self.update_interface(self.mesa.get_estado_partida())
            dict = self.montar_dict()
            dict['match_status'] = "next"
            self.dog_server_interface.send_move(dict)

    def completar_missao(self, event):
        message = self.mesa.completar_missao()

        messagebox.showinfo(message=message)
        if self.mesa.get_estado_partida() == 3:
            self.update_interface(self.mesa.get_estado_partida())
            dict = self.montar_dict()
            dict['match_status'] = "next"
            self.dog_server_interface.send_move(dict)
        if self.mesa.get_estado_partida() == 4:
            self.update_interface(self.mesa.get_estado_partida())
            dict = self.montar_dict()
            dict['match_status'] = "finalize"
            self.dog_server_interface.send_move(dict)

    def trocar_missao(self, event):
        message = self.mesa.trocar_missao()
        if message is not None:
            messagebox.showinfo(message=message)
        else:
            self.update_interface(self.mesa.get_estado_partida())
            dict = self.montar_dict()
            dict['match_status'] = "next"
            self.dog_server_interface.send_move(dict)
        
    def start_match(self):
        start_status = self.dog_server_interface.start_match(2)
        code = start_status.get_code()
        message = start_status.get_message()
        if code == "2":
            players = start_status.get_players()
            local_player_id = start_status.get_local_id()
            self.mesa.start_match(players, local_player_id)
            dict = self.montar_dict()
            dict['match_status'] = "progress"
            self.dog_server_interface.send_move(dict)
            print("Mandou Infos")
            messagebox.showinfo(message=message)
            self.update_interface(self.mesa.get_estado_partida())
        elif code == "0" or code == "1":
            messagebox.showinfo(message=message)

    def receive_start(self, start_status):
        print("recebeu inicio")
        message = start_status.get_message()
        messagebox.showinfo(message=message)
        players = start_status.get_players()
        local_player_id = start_status.get_local_id()
        self.mesa.receive_start(players, local_player_id)
    
    def receive_withdrawal_notification(self):
        messagebox.showinfo(message="Oponente declarou desistência")
        sys.exit(0)

    def receive_move(self, a_move):
        self.mesa.receive_move(a_move)
        self.update_interface(self.mesa.get_estado_partida())
        if (a_move['match_status'] == 'finalize'):
            messagebox.showinfo(message="Você perdeu :(")

    def montar_dict(self):
        estado_partida = self.mesa.get_estado_partida()
        if estado_partida == 0 or estado_partida == 1:
            self.localplayer_info = self.mesa.get_localplayer_info()
            self.remoteplayer_info = self.mesa.get_remoteplayer_info()
            dict_jogada = {}
            dict_jogada['carta0_A'] = self.localplayer_info[0][0].cardimage
            dict_jogada['carta1_A'] = self.localplayer_info[0][1].cardimage
            dict_jogada['carta2_A'] = self.localplayer_info[0][2].cardimage
            dict_jogada['carta3_A'] = self.localplayer_info[0][3].cardimage
            dict_jogada['carta4_A'] = self.localplayer_info[0][4].cardimage
            dict_jogada['carta0_B'] = self.remoteplayer_info[0][0].cardimage
            dict_jogada['carta1_B'] = self.remoteplayer_info[0][1].cardimage
            dict_jogada['carta2_B'] = self.remoteplayer_info[0][2].cardimage
            dict_jogada['carta3_B'] = self.remoteplayer_info[0][3].cardimage
            dict_jogada['carta4_B'] = self.remoteplayer_info[0][4].cardimage

            dict_jogada['pizzas_A'] = self.localplayer_info[1]
            dict_jogada['pizzas_B'] = self.remoteplayer_info[1]

            dict_jogada['area_entrega_A'] = self.localplayer_info[2]
            dict_jogada['area_entrega_B'] = self.remoteplayer_info[2]

            dict_jogada['missao_A'] = self.localplayer_info[3].cardimage
            dict_jogada['missao_B'] = self.remoteplayer_info[3].cardimage

            return dict_jogada
        else:
            # montagem do dicionario para inicialização de um jogador remoto
            # get_player_info: 0-Cartas, 1-Pizzas, 2- Area de Entrega, 3-Missão
            self.player_info = self.mesa.get_localplayer_info()
            dict_jogada = {}

            #insere cartas no dicionario
            card_count = 0
            for carta in self.player_info[0]:
                dict_jogada[str(card_count)] = carta.cardimage
                card_count = card_count + 1
            
            dict_jogada['pizzas'] = self.player_info[1]
            dict_jogada['area_entrega'] = self.player_info[2]
            dict_jogada['missao'] = self.player_info[3].cardimage
            #keyerror - try-catch
            #print(dict_jogada['aaa'])
            return dict_jogada

