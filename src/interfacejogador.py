from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from mesa import Mesa
from dog.dog_interface import DogPlayerInterface
from dog.dog_actor import DogActor

class InterfaceJogador(DogPlayerInterface):
    def __init__(self):
        self.main_window = Tk()  # instanciar Tk
        self.fill_main_window()  # organização e preenchimento da janela
        self.board = Mesa()  # tratamento do domínio do problema

    
    # Popula a janela Tk com os elementos
    def fill_main_window(self):
        self.main_window.title("Jogo da Pizza")
        #self.main_window.iconbitmap("src/images/icon.ico")
        self.main_window.geometry("1280x720")
        self.main_window.resizable(False, False)
        #self.main_window["bg"] = "gold3"