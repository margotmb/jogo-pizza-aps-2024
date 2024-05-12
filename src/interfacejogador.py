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
        # Organização e preenchimento da janela  
        self.fill_main_window()

        # Tratamento do domínio do problema
        self.mesa = Mesa()

        # Recebe o estado da partida e atualiza interface de acordo
        estado_partida = self.mesa.get_status()
        self.atualiza_interface(estado_partida)

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
        self.main_window.title("Jogo da Pizza")
        #self.main_window.iconbitmap("src/images/icon.ico")
        self.main_window.resizable(False, False)
        self.main_window.geometry("1280x720")
        #self.main_window["bg"] = 'gold3'

        self.bg_img = PhotoImage(file="src/images/init_bg.png")
        self.bg_label = Label(self.main_window, image = self.bg_img)
        self.bg_label.place(x=0,y=0)
        
        

        self.start_button = Label(self.main_window, text = "Iniciar Partida", width=100, height=100, borderwidth=2, relief="groove")
        self.start_button.place(width=150, height=50, anchor='center', relx=0.5, rely=0.55)
        self.start_button.bind("<Button-1>", lambda e: self.start_match())

        # Frame principal - mock
        #self.main_frame = Frame(self.main_window, width=1280, height=720)
        #self.main_frame.grid(row=0, column=0)
        #self.main_frame.grid(row=0, column=0)
        #self.img_mockup_interface = PhotoImage(file="src/images/mockup.png")
        #self.main_label = Label(self.main_frame, bg='red', image=self.img_mockup_interface)
        #self.main_label.place(relx=0.5, rely=0.5, anchor = 'center')


    def main_game_screen(self):
        self.start_button.destroy()
        
        #Disposição da Interface: Ver template_interface.png
        #Estado atual: produzindo a interface em sua versão template.
        #Futuramente alterar para receber essas informações através da mesa

        #Frame oponente
        self.frame_oponente = Frame(self.main_window, width=1280, height=250, bg="red")
        self.frame_oponente.grid(row=0, column=0)

        #Frame: pizza_missao_oponente
        self.frame_pizza_missao_oponente = Frame(self.frame_oponente, width=700, height=250)
        self.frame_pizza_missao_oponente.grid(row=0, column=0)

        #Label Missao
        self.img_missao_oponente = PhotoImage(file="src/images/missao1-2.png")
        self.missao_oponente = Label(self.frame_pizza_missao_oponente, 
                                           bg='red', 
                                           #text="label_missao_oponente",
                                           image=self.img_missao_oponente
                                           )
        self.missao_oponente.place(width=300, height=250, x=0, y=0)
        

        #Label Pizzas
        self.img_pizza_oponente = PhotoImage(file="src/images/pizza16.png")
        self.pizza_oponente = Label(self.frame_pizza_missao_oponente,
                                          bg='maroon',
                                          image=self.img_pizza_oponente)
        self.pizza_oponente.place(width=400, height=250, x=300, y=0)

        # Frame: oponente_fracoes
        self.frame_oponente_fracoes = Frame(self.frame_oponente, width=580, height=250, bg='red')
        self.frame_oponente_fracoes.grid(row=0, column=1)

        #Labels Carta Fração -> popula um array de cartas
        self.cartas_fracao_oponente = []
        self.img_carta_fracao_oponente = PhotoImage(file="src/images/fracao1-4.png")
        x_pos = 20
        for i in range(0,5):
            a_Label = Label(self.frame_oponente_fracoes, image=self.img_carta_fracao_oponente, bg="red")
            self.cartas_fracao_oponente.append(a_Label)
            self.cartas_fracao_oponente[i].place(width=100, height=250, x=x_pos, y = 0)
            x_pos = x_pos + 110

        # -----
        #Frame central -> Frame Baralhos -> label:baralho_fracoes, label: baralho_missoes
        self.frame_central = Frame(self.main_window, width=1280, height=220, bg="khaki1")
        self.frame_central.grid(row=1, column=0)

        self.baralho_fracoes = Label(self.frame_central, text="baralho_fracoes", bg='yellow', borderwidth=2, relief="solid")
        self.baralho_fracoes.place(width=300, height=220, x=340, y=0)

        self.baralho_missoes = Label(self.frame_central, text="baralho_missoes", bg="green", borderwidth=2, relief="solid")
        self.baralho_missoes.place(width=300, height=220, x=660, y=0)
        # ----


        #Frame jogador
        self.frame_jogador = Frame(self.main_window, width=1280, height=250, bg="blue")
        self.frame_jogador.grid(row=2, column=0)

        #jogador_fracoes
        self.frame_jogador_fracoes = Frame(self.frame_jogador, width=580, height=250, bg='blue')
        self.frame_jogador_fracoes.grid(row=0, column=0)

        #Labels Carta Fração -> popula um array de cartas
        self.cartas_fracao_jogador= []
        self.img_carta_fracao_jogador = PhotoImage(file="src/images/fracao1-4.png")
        x_pos = 20
        for i in range(0,5):
            a_Label = Label(self.frame_jogador_fracoes, image=self.img_carta_fracao_jogador, bg="blue")
            self.cartas_fracao_jogador.append(a_Label)
            self.cartas_fracao_jogador[i].place(width=100, height=250, x=x_pos, y = 0)
            x_pos = x_pos + 110

        self.frame_pizza_missao_jogador = Frame(self.frame_jogador, width=700, height=250)
        self.frame_pizza_missao_jogador.grid(row=0, column=1)

        # pizza_jogador
        self.img_pizza_jogador = PhotoImage(file="src/images/pizza16.png")
        self.pizza_jogador = Label(self.frame_pizza_missao_jogador,
                                         bg='navyblue',
                                        image=self.img_pizza_jogador)
        self.pizza_jogador.place(width=400, height=250, x=0, y=0)

        # missao_jogador
        self.img_missao_jogador = PhotoImage(file="src/images/missao1-2.png")
        self.missao_jogador = Label(self.frame_pizza_missao_jogador,
                                          bg="blue",
                                          image=self.img_missao_jogador)
        self.missao_jogador.place(width=300, height=250, x=400, y=0)


    def atualiza_interface(self, estado_partida):
        NotImplemented
    
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
