# maquina de gifs v.3 : A partir de subtitulos de youtube
# youtube-dl --write-auto-sub https://www.youtube.com/watch?v=6ATS7k_LKEc&t=6s

from moviepy.editor import *
from BeautifulSoup import BeautifulSoup

archivo = open("videos/trump.vtt")
archivoTexto= archivo.read()


lineas=archivoTexto.split('\n')

for indice,linea in enumerate(lineas):
    if "-->" in linea:
        
        texto = lineas[indice+1]
        textoLimpio = BeautifulSoup(texto).text
        
        if "china".upper() in texto.upper():
            
            empieza = linea[0:11]
            acaba = linea[17:29]
            
            print empieza
            print acaba
            print texto
            
            #creamos el clip
            clip=VideoFileClip("trump.webm").subclip(empieza,acaba).resize(width=300)
            #clip.write_videofile(str(indice)+".mp4")
            clip.write_gif(str(indice)+".gif",fps=8,program='ImageMagick',opt='OptimizeTransparency')


print "FIN"