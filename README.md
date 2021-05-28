# baixar_musicas_python

Este simples projeto tem como objetivo criar um pequeno programa para extrair e salvar
uma música através de um vídeo do Youtube.

## Requisitos para criar o programa

- Ter o Python 3.6+ instalado em sua máquina
- Uma IDE de preferência
- Realizar a instalação dos pacotes descritos abaixo(alguns já são nativos da linguagem)

```bash
from tkinter import *
from tkinter import messagebox
from pytube import YouTube
from moviepy.audio.io.AudioFileClip import AudioFileClip
import urllib.request, urllib.parse, urllib.error
import re
import os
```
### OBS

As vezes a Lib pytube pode dar erro '404', apenas de uma pequena pesquisada para saber se foi corrigido.
Após conferir, desinstale e instale novamente.
## Desenvolvimento do projeto

O projeto é estruturado de uma forma simples de modo que seja fácil para que outros estudantes
realizem o mesmo procedimento.

Para uma melhor organização, crie uma pasta para guardar os itens que serão apresentados

### Arquivo app.py

Este arquivo compõe todo o código da aplicação. Temos duas classes criadas, chamadas
**Application** e **Baixar_mp3**.

Na classe **Application** temos um pequeno código utilizando a Lib tinker, nativa do próprio Python,
para a criação de uma pequena interface gráfica para o projeto. Existe também uma pequena interação
com botão para realizar o download.

![Imagem interface gráfica](./interface.png)

Já a clase **Baixar_mp3** é onde temos o código para executar a tarefa em si. Nela existem 2 métodos
criados, um para baixar a música em MP4, seguindo do outro para converter para MP3. Ainda nesta classe
são utilizadas as bibliotecas **pytube**, **moviepy**, **urllib**, **re** e **os**.

Ainda compondo o arquivo, temos uma função definida como **main** e a chamada através do 
```bash
if __name__ == "__main__":
    main()
```

### Pasta music

Essa pasta foi criada para ser a rota de armazenamento das músicas já convertidas em MP3. Se lido 
o código na classe **Baixar_mp3**, é vista uma variável com o nome path.


## Como executar

Para executar e aparecer o pequeno aplicativo, basta dar um RUN pela IDE ou escrever um comando
no terminal
```bash
python3 app.py
```
Após realizar o start, abra um video, copie sua URL e cole no local onde a aplicação sugere.