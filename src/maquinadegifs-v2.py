from moviepy.editor import *
import numpy as np
import cv2

segundosDuracion=3

segundosParaCrearGifs=[]
frameCount=0

videoURL='videos/pimpflaco.mkv'

cap = cv2.VideoCapture(videoURL)
fps = int(cap.get(5))

print fps

while(cap.isOpened()):
    
    frameCount+=1
    
    #leer cada frame del video
    ret, frame = cap.read()
    
    #hacer el reproductor mas pequeno
    frame=cv2.resize(frame,None,fx=0.5, fy=0.5)
    cv2.imshow('frame',frame)
    
    #escuchamos teclas
    teclaPulsada= cv2.waitKey(fps)
    
    if teclaPulsada == ord('g'):
        
        segundoCaptura=frameCount/fps
        
        print segundoCaptura
        segundosParaCrearGifs.append(segundoCaptura)
        
    if teclaPulsada == ord('q'):
        break
  
 
print segundosParaCrearGifs

#vamos a crear los gifs

mainclip=VideoFileClip(videoURL)

for segundo in segundosParaCrearGifs:
    empieza = segundo
    acaba = segundo+segundosDuracion
    clip = mainclip.subclip(empieza,acaba).resize(width=400)
    clip.write_gif("gifs/pimpflaco"+str(segundo)+".gif",fps=10,program='ImageMagick',opt='optimizeplus')

cap.release()
cv2.destroyAllWindows()