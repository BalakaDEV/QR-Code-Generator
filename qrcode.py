#Faça a instalação das bibliotecas no cmd (pip install pyqrcode // pip install pypng)
import pyqrcode
import png
#Restart e Validação
import os
import sys
import os.path
from PIL import Image

#Reiniciar Aplicação
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

#Gerador + Validação do link
link = input("Coloque o link do site:")

if link.startswith('https://'):
  print("Link Validado")
elif link.endswith('.com'):
  print("Link Valido")
elif link.endswith('.br'):
  print("Link Validado")
else:
  print("Link Recusado. Tente Novamente")
  restart_program()  

#Inclusão de nome na imagem + Validação
arquivo = input("Coloque o nome do arquivo:")
if os.path.exists(f"{arquivo}.png"):
    print("O arquivo já existe tente outro nome")
    restart_program()  


#Url do QRCODE
site = f"{link}"

#Criação da URL
url = pyqrcode.create(site)

#Criação da imagem do QRCODE
url.png(f"{arquivo}.png", scale=5)

print("QRCODE Criado na pasta do arquivo!")