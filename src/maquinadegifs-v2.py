from moviepy.editor import *
import moviepy.video.io.preview as preview
import pygame as pg
import numpy as np
import sys

mainClip=VideoFileClip("videos/test.mp4")

segundosDuracion=3

screen = pg.display.set_mode((mainClip.size))

for segundo in np.arange(1.0 / mainClip.fps, mainClip.duration-.001, 1.0 / mainClip.fps):
    img = mainClip.get_frame(segundo)
    
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            
            if event.key == pg.K_ESCAPE:
                sys.exit()
            
            if event.key == pg.K_SPACE: #tecla G
                print "captura en segundo "+str(segundo)
                
                empieza=segundo
                acaba=segundo+segundosDuracion
                clip = mainClip.subclip(empieza,acaba).resize(width=400)
                clip.write_gif("gifs/test"+str(segundo)+".gif",fps=10,program='ImageMagick',opt='optimizeplus')
    
    #dibujar pantalla
    preview.imdisplay(img, screen)
