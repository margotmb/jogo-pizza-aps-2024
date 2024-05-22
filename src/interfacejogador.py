from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from mesa import Mesa
from dog.dog_interface import DogPlayerInterface
from dog.dog_actor import DogActor


class InterfaceJogador(DogPlayerInterface):
    def __init__(self):
        # Instanciar Tk
        self.main_window = Tk()
        self.mesa = Mesa()# Tratamento do domínio do problema
        self.test_var = 0
        # Organização e preenchimento da janela  
        self.fill_main_window()

        # Set Player Name
        player_name = simpledialog.askstring(title="Player identification", prompt="Qual o seu nome?")

        # Dog 
        #self.dog_server_interface = DogActor()
        #message = self.dog_server_interface.initialize(player_name, self)
        #messagebox.showinfo(message=message)

        text_string = "Olá, " + player_name + "\n\n Clique no botão abaixo para começar"
        self.player_name = Label(self.main_window, text=text_string, bg="khaki1", borderwidth=3, relief="ridge")
        self.player_name.place(width = 300, height=100, anchor='center', relx=0.5, rely=0.4)

        # Main Loop
        self.main_window.mainloop()

    
    # Popula a janela Tk com os elementos
    def fill_main_window(self):
        estado_partida = self.mesa.get_status()
        self.main_window.title("Jogo da Pizza")
        #self.main_window.iconbitmap("src/images/icon.ico")
        self.main_window.resizable(False, False)
        self.main_window.geometry("1280x720")

        self.bg_img = PhotoImage(file="src/images/init_bg.png")
        self.bg_label = Label(self.main_window, image = self.bg_img)
        self.bg_label.place(x=0,y=0)
        
        self.start_button = Label(self.main_window, text = "Iniciar Partida", width=100, height=100, borderwidth=2, relief="groove")
        self.start_button.place(width=150, height=50, anchor='center', relx=0.5, rely=0.55)
        #self.start_button.bind("<Button-1>", lambda e: self.start_match())
        self.start_button.bind("<Button-1>", lambda e: self.update_interface(estado_partida))



    def update_interface(self,estado_partida):
        if estado_partida == 1:
            self.start_button.destroy()
        
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
        self.pizza_oponente.place(width=400, height=250, x=300, y=0)
        self.pizza_oponente.bind("<Button-1>", lambda e: print('aaa'))
        
        # -- Frame Cartas
        self.frame_cartas_oponente = Frame(self.frame_oponente, width=600, height=250, bg="green")

        self.cartas_fracao_oponente = self.mesa.get_remote_cartas()
        self.img_carta_fracao_oponente = []
        
        # -- 
        
        # -----
        #Frame central -> Frame Baralhos -> label:baralho_fracoes, label: baralho_missoes
        self.frame_central = Frame(self.main_window, width=1280, height=220, bg="khaki1")
        self.frame_central.grid(row=1, column=0)

        self.baralho_fracoes = Label(self.frame_central, text="baralho_fracoes", bg='yellow', borderwidth=2, relief="solid")
        self.baralho_fracoes.place(width=300, height=220, x=340, y=0)
        self.baralho_fracoes.bind("<Button-1>", self.comprar_carta)

        self.baralho_missoes = Label(self.frame_central, text="baralho_missoes", bg="green", borderwidth=2, relief="solid")
        self.baralho_missoes.place(width=300, height=220, x=660, y=0)
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
        
        #Atribui bind handle_click às labels
        for a in self.label_cartasjogador:
            #print(a.cget("text"))
            a.bind("<Button-1>", self.handle_click)

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

        area_entrega = self.localplayer_info[2]
        txt = "Area Entrega: " + str(area_entrega) + " fatias prontas"
        self.area_entrega = Label(self.frame_jogador,
                                  bg='pink',
                                  text=txt 
                                  )
        self.area_entrega.place(width=400, height=50, x=620, y=0)


        # missao_jogador
        #self.localplayer_info[3]
        self.img_missao_jogador = PhotoImage(file="src/images/missao1-2.png")
        self.missao_jogador = Label(self.frame_jogador,
                                          bg="blue",
                                          image=self.img_missao_jogador)
        self.missao_jogador.place(width=200, height=250, x=1050, y=0)


    def fatiar_pizza(self):
        # manda comando pra fatiar pizza -> self.mesa.fatiar_pizza()
        # re-renderiza interface -> self.update_interface(5)
        # chama função de enviar info pro oponente
        print("whoosh")

    def handle_click(self, event):
        #objeto EVENT tem uma referencia ao widget label que está atrelado ao clique
        #print(event.widget.cget("text"))
        num = event.widget.cget("text")
        self.mesa.fatiar_pizza(num)
        self.update_interface(2)

    def comprar_carta(self, event):
        message = self.mesa.comprar_carta()
        if message is not None:
            messagebox.showinfo(message=message)
        self.update_interface(2)

    def start_match(self):
        start_status = self.dog_server_interface.start_match(2)
        message = start_status.get_message()
        messagebox.showinfo(message=message)
        if (start_status.get_code() == "2"):
            self.main_game_screen()

    def receive_start(self, start_status):
        message = start_status.get_message()
        messagebox.showinfo(message=message)
        self.main_game_screen()
