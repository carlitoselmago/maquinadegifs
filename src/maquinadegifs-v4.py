# maquina de gifs v.4 : A partir de subtitulos de series

from moviepy.editor import *
import os

carpeta="/home/haxoorx/Downloads/SUBTITLESUBTILITIES/SERIES/LOST/Season 1/"


def getFiles(sourceFolder):
        files=[]
        for root, dir, file in os.walk(sourceFolder):
            if len(file)>0:
                files.append(file)
        return files[0]

archivos=getFiles(carpeta)

for NombreArchivo in archivos:
    
    print NombreArchivo
    
    if ".srt" in NombreArchivo:
        
        archivo = open(carpeta+NombreArchivo)
        archivoTexto= archivo.read()

        lineas=archivoTexto.split('\n')

        for indice,linea in enumerate(lineas):

            if "whirring".upper() in linea.upper():

                texto=linea

                lineaDeTiempo=False

                if "-->" in lineas[indice-1]:
                    lineaDeTiempo=lineas[indice-1]
                if "-->" in lineas[indice-2]:
                    lineaDeTiempo=lineas[indice-2]

                if lineaDeTiempo:
                    empieza = lineaDeTiempo[0:11]
                    acaba = lineaDeTiempo[17:29]

                    print empieza
                    print acaba
                    print texto

                    #creamos el clip
                    
                    videoFilename=NombreArchivo.replace(".srt",".mkv")
                    
                    clip=VideoFileClip(carpeta+videoFilename).subclip(empieza,acaba).resize(width=300)
                    #clip.write_videofile(str(indice)+".mp4")
                    clip.write_gif("gifs/LOST"+str(indice)+".gif",fps=8,program='ImageMagick',opt='OptimizeTransparency')


print "FIN"