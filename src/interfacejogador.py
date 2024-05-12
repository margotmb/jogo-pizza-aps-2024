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

        # Main Loop
        self.main_window.mainloop()

    
    # Popula a janela Tk com os elementos
    def fill_main_window(self):
        self.main_window.title("Jogo da Pizza")
        #self.main_window.iconbitmap("src/images/icon.ico")
        self.main_window.resizable(False, False)
        #self.main_window["bg"] = "gold3"
        
        self.main_frame = Frame(self.main_window, width=1280, height=720)
        self.main_frame.grid(row=0, column=0)

        self.img_mockup_interface = PhotoImage(file="src/images/mockup.png")
        self.main_label = Label(self.main_frame, bg='red', image=self.img_mockup_interface)
        self.main_label.place(relx=0.5, rely=0.5, anchor = 'center')

        #self.enemy_frame_cards = Frame(self.main_window, width=426, height=250, bg="red")
        #self.enemy_frame_cards.grid(row=0, column=0)

        #self.enemy_frame = Frame(self.main_window, width=1280, height=250, bg="red")
        #self.enemy_frame.grid(row=0, column=0)

        #self.frame_baralhos = Frame(self.main_window, width=1280, height=220, bg="white")
        #self.frame_baralhos.grid(row=1, column=0)

        #self.player_frame = Frame(self.main_window, width=1280, height=250, bg="blue")
        #self.player_frame.grid(row=2, column=0)

        #self.img_fracao_oponente = PhotoImage(file="src/images/fracao1-4.png") 
        #self.fracao_oponente = Label(self.enemy_frame, bg='red', image=self.img_fracao_oponente)
        #self.fracao_oponente.place(relx=0.3, rely=0.5, anchor = 'e')

        #self.img_missao_oponente = PhotoImage(file="src/images/missao1-2.png")
        #self.missao_oponente = Label(self.enemy_frame, bg='red', image=self.img_missao_oponente)
        #self.missao_oponente.place(relx=0.9, rely=0.5,anchor = 'center')
        #self.missao_oponente.bind("<Button-1>",lambda e:print("123"))

    def atualiza_interface(self, estado_partida):
        NotImplemented