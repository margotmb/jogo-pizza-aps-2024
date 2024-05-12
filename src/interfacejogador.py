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
        #player_name = simpledialog.askstring(title="Player identification", prompt="Qual o seu nome?")
        

        # Dog 
        #self.dog_server_interface = DogActor()
        #message = self.dog_server_interface.initialize(player_name, self)
        #messagebox.showinfo(message=message)

        # Main Loop
        self.main_window.mainloop()

    
    # Popula a janela Tk com os elementos
    def fill_main_window(self):
        self.main_window.title("Jogo da Pizza")
        #self.main_window.iconbitmap("src/images/icon.ico")
        self.main_window.resizable(False, False)
        #self.main_window["bg"] = "gold3"
        
        # Frame principal
        self.main_frame = Frame(self.main_window, width=1280, height=720)

        #self.main_frame.grid(row=0, column=0)
        #self.img_mockup_interface = PhotoImage(file="src/images/mockup.png")
        #self.main_label = Label(self.main_frame, bg='red', image=self.img_mockup_interface)
        #self.main_label.place(relx=0.5, rely=0.5, anchor = 'center')


        #Disposição da Interface: Ver template_interface.png
        #Estado: produzindo a interface em seu estado template.
        #Futuramente alterar para receber essas informações informações através da mesa


        #Frame oponente -> Frame pizza_missao_oponente, Frame oponente frações
        self.frame_oponente = Frame(self.main_window, width=1280, height=250, bg="red")
        self.frame_oponente.grid(row=0, column=0)

        #Espaço no lado oponente onde fica a missão e as pizzas
        self.frame_pizza_missao_oponente = Frame(self.frame_oponente, width=700, height=250, bg="green")
        self.frame_pizza_missao_oponente.grid(row=0, column=0)

        #Label Missao
        self.img_missao_oponente = PhotoImage(file="src/images/missao1-2.png")
        self.label_missao_oponente = Label(self.frame_pizza_missao_oponente, 
                                           bg='red', 
                                           #text="label_missao_oponente",
                                           image=self.img_missao_oponente
                                           )
        self.label_missao_oponente.place(width=300, height=250, x=0, y=0)
        

        #Label Pizzas
        self.img_pizza_oponente = PhotoImage(file="src/images/pizza16.png")
        self.label_pizza_oponente = Label(self.frame_pizza_missao_oponente,
                                          bg='purple',
                                          image=self.img_pizza_oponente)
        self.label_pizza_oponente.place(width=400, height=250, x=300, y=0)

        # Frame Frações Oponente
        self.frame_oponente_fracoes = Frame(self.frame_oponente, width=580, height=250, bg="yellow")
        self.frame_oponente_fracoes.grid(row=0, column=1)

        #Labels Carta Fração -> popula um array de cartas
        self.labels_carta_fracao = []
        self.img_carta_fracao = PhotoImage(file="src/images/fracao1-4.png")
        x_pos = 20
        for i in range(0,5):
            a_Label = Label(self.frame_oponente_fracoes, image=self.img_carta_fracao)
            self.labels_carta_fracao.append(a_Label)
            self.labels_carta_fracao[i].place(width=100, height=250, x=x_pos, y = 0)
            x_pos = x_pos + 110

        #Frame central -> Frame Baralhos -> label:baralho_fracoes, label: baralho_missoes
        self.frame_central = Frame(self.main_window, width=1280, height=220, bg="white")
        self.frame_central.grid(row=1, column=0)

        self.frame_jogador = Frame(self.main_window, width=1280, height=250, bg="blue")
        self.frame_jogador.grid(row=2, column=0)


        #self.img_fracao_oponente = PhotoImage(file="src/images/fracao1-4.png") 
        #self.fracao_oponente = Label(self.enemy_frame, bg='red', image=self.img_fracao_oponente)
        #self.fracao_oponente.place(relx=0.3, rely=0.5, anchor = 'e')

        #self.img_missao_oponente = PhotoImage(file="src/images/missao1-2.png")
        #self.missao_oponente = Label(self.enemy_frame, bg='red', image=self.img_missao_oponente)
        #self.missao_oponente.place(relx=0.9, rely=0.5,anchor = 'center')
        #self.missao_oponente.bind("<Button-1>",lambda e:print("123"))

    def atualiza_interface(self, estado_partida):
        NotImplemented