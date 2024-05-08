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
        self.board = Mesa()  

        # Set Player Name
        player_name = simpledialog.askstring(title="Player identification", prompt="Qual o seu nome?")
        self.dog_server_interface = DogActor()

        # Dog Response
        message = self.dog_server_interface.initialize(player_name, self)
        messagebox.showinfo(message=message)

        # Main Loop
        self.main_window.mainloop()

    
    # Popula a janela Tk com os elementos
    def fill_main_window(self):
        self.main_window.title("Jogo da Pizza")
        #self.main_window.iconbitmap("src/images/icon.ico")
        self.main_window.geometry("1280x720")
        self.main_window.resizable(False, False)
        self.main_window["bg"] = "white"


        self.table_frame = Frame(self.main_window, padx=100, pady=40, bg="gold3")
        self.table_frame.grid(row=0, column=0)
        self.message_frame = Frame(self.main_window, padx=0, pady=10, bg="gold3")
        self.message_frame.grid(row=1, column=0)

        #self.table_frame = Frame(self.main_window, padx=100, pady=40, bg="gold3")
        #self.table_frame.grid(row=0, column=0)
        #self.message_frame = Frame(self.main_window, padx=0, pady=10, bg="gold3")
        #self.message_frame.grid(row=1, column=0)