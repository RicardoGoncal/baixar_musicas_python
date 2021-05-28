# -*- coding: utf-8 -*-

"""
    aplicativo para realizar o download do youtube e 
    salvar em uma pasta especifica
"""

from tkinter import *
from tkinter import messagebox
from pytube import YouTube
from moviepy.audio.io.AudioFileClip import AudioFileClip
import urllib.request, urllib.parse, urllib.error
import re
import os

class Application:
    def __init__(self, master=None):

        """
            Classe responsável por criar uma pequena
            interface gráfica com o tkinter
        """

        self.master = master
        self.master.title('Baixa musica Youtube')
        self.master['bg'] = 'red'
        self.master.resizable(False, False)
        self.ms = "....."
        
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer['pady'] = 10
        self.primeiroContainer['bg'] = 'red'
        self.primeiroContainer.pack()
        

        self.segundoContainer = Frame(master)
        self.segundoContainer['padx'] = 20
        self.segundoContainer['bg'] = 'red'
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer['padx'] = 20
        self.terceiroContainer['pady'] = 10
        self.terceiroContainer['bg'] = 'red'
        self.terceiroContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="Cole o link do youtube para baixar a musica", fg='white')
        self.titulo['font'] = ("Arial", "10", "bold")
        self.titulo['bg'] = 'red'
        self.titulo.pack()

        self.nomeLink = Label(self.segundoContainer, text="Link do youtube", font=self.fontePadrao, fg='white')
        self.nomeLink['bg'] = 'red'
        self.nomeLink.pack(side=LEFT)

        self.link = Entry(self.segundoContainer)
        self.link['width'] = 30
        self.link['font'] = self.fontePadrao
        # self.link['bg'] = 'red'
        self.link.pack(side=LEFT)

        self.download = Button(self.terceiroContainer)
        self.download['text'] = "Download"
        self.download['font'] = ('Calibri', '8')
        self.download['width'] = 12
        self.download['command'] = self.download_mp3
        self.download.pack()

        self.msg = Label(self.terceiroContainer, text=self.ms, font=self.fontePadrao, fg='white')
        self.msg['bg'] = 'red'
        self.msg.pack()


    # Método para baixar a musica do youtube
    def download_mp3(self):
        
        link = self.link.get()
        mp3 = Baixar_mp3(link)
        musica = mp3.baixar_musica()
        
        if musica:
            self.ms = musica
            messagebox.showinfo(title="Resposta", message=self.ms)

        
        self.clear_text()
        
    def clear_text(self):
        self.link.delete(0, 'end')



class Baixar_mp3:
    
    """
        Classe que executa o download e converte a música
        vinda do Youtube
    """
    
    def __init__(self, link):
        self.link = link
        self.path = './music/'

    def baixar_musica(self):

        try:
            yt = YouTube(self.link)
            print('baixando musica....')
            ys = yt.streams.filter(only_audio=True).first().download(self.path)
            
            self.converte_mp4()

            return 'Download completo!'
        except urllib.error.HTTPError:
            return 'Erro, 1 - repita novamente o processo\n2 - cole um link diferente se erro novamente'

    def converte_mp4(self):
        mp = AudioFileClip
        print('Convetendo arquivo')
        for file in os.listdir(self.path):
            if re.search('mp4', file):
                mp4_path = os.path.join(self.path,file)
                mp3_path = os.path.join(self.path, os.path.splitext(file)[0]+'.mp3')
                new_file = mp(mp4_path)
                new_file.write_audiofile(mp3_path)
                os.remove(mp4_path)



def main():
    root = Tk()
    Application(root)
    root.mainloop()


if __name__ == "__main__":
    main()