import pygame,string,random,time,sys
B="el juego culmina al perderlas todas, así verá su puntaje final. ¡Buena suerte!"
A="Instrucciones: Escriba una palabra que contenga las letras disponibles por REBELS,"
c="usted tendrá tres vidas para conseguirlo; cada vez que se equivoque perderá una vida,"
corre="correcto"
error="error"
gamo="game over"
cont="¿desea continuar? "
clos="close"
restart="si"
pygame.quit()
pygame.init()
punt=0
vida=3
restart="si"
done=False
size= (1200, 675)
screen=pygame.display.set_mode(size)
fuente=pygame.font.Font(None,30)
fuente2=pygame.font.Font(None,100)
Atexto=fuente.render(A,0,(250,250,250))
Ctexto=fuente.render(c,0,(250,250,250))
Btexto=fuente.render(B,0,(250,250,250))
palabra=fuente.render(c,0,(250,250,250))
corre=fuente2.render(corre,0,(250,250,250))
error=fuente2.render(error,0,(250,250,250))
gamo=fuente2.render(gamo,0,(250,250,250))
cont=fuente2.render(cont,0,(250,250,250))
clos=fuente2.render(clos,0,(250,250,250))
estre=pygame.image.load("fondo1.jpg").convert()
muer=pygame.image.load("estre.jpg").convert()
logo=pygame.image.load("logo.jpg").convert()
ok=pygame.image.load("botonok.jpg").convert()
titlr=pygame.image.load("titlr.webp").convert()
lose=pygame.image.load("gameover.png").convert()
screen.blit(estre, [0,0])
screen.blit(ok, [544,517])
screen.blit(titlr, [505,317])
screen.blit(logo, [505,195])
screen.blit(Atexto,(159,105))
screen.blit(Ctexto,(153,135))
screen.blit(Btexto,(200,165))
pygame.display.flip()
pygame.display.flip()
while not done:
    for event in pygame.event.get():
        print(event)
        if event.type==pygame.QUIT:
            done=True
        if(restart=="no"):
            done=True
        if event.type==pygame.MOUSEBUTTONDOWN:
            screen.blit(muer,[0,0])
            pygame.display.flip()
            while True:
                    if(restart=="si"):
                        while True:
                            rand1 = random.choice(string.ascii_letters)
                            rand1=rand1.lower()
                            rand2 = random.choice(string.ascii_letters)
                            rand2=rand2.lower()
                            rand3 = random.choice(string.ascii_letters)
                            rand3=rand3.lower()
                            if(punt>=0 and  punt<500):
                                palabra1=rand1
                                palabra1=fuente2.render(palabra1,0,(250,250,250))
                                screen.blit(palabra1,(600,165))
                                pygame.display.flip()
                                print(palabra1)
                                A=str(input())
                                p=list(A)
                                if ((rand1 in p)==True):
                                    screen.blit(corre,(560,475))
                                    pygame.display.flip()
                                    print("correcto")
                                    punt=punt+50
                                else:
                                    screen.blit(error,(570,475))
                                    pygame.display.flip()
                                    print("error")
                                    vida=vida-1
                            if(punt>=500 and  punt<1500):
                                palabra2=rand1,rand2
                                palabra2=fuente2.render(palabra2,0,(250,250,250))
                                screen.blit(palabra2,(590,165))
                                pygame.display.flip()
                                print(palabra2)
                                A=str(input())
                                p=list(A)
                                if ((rand1 and rand2 in p)==True):
                                    screen.blit(corre,(560,475))
                                    pygame.display.flip()
                                    print("correcto")
                                    punt=punt+50
                                else:
                                    screen.blit(error,(570,475))
                                    pygame.display.flip()
                                    print("error")
                                    vida=vida-1
                            if(punt>=1500):
                                palabra3=rand1,rand2,rand3
                                palabra3=fuente2.render(palabra3,0,(250,250,250))
                                screen.blit(palabra3,(580,165))
                                pygame.display.flip()
                                print(palabra3)
                                A=str(input())
                                p=list(A)
                                if ((rand1 and rand2 and rand3 in p)==True):
                                    screen.blit(corre,(560,475))
                                    pygame.display.flip()
                                    print("correcto")
                                    punt=punt+50
                                else:
                                    screen.blit(error,(570,475))
                                    pygame.display.flip()
                                    print("error")
                                    vida=vida-1
                            if(vida==0):
                                screen.blit(lose,(0,0))
                                screen.blit(gamo,(540,165))
                                pygame.display.flip()
                                print("game over")
                                break
                        supu=("su puntaje fue de: ",punt)
                        supu=fuente2.render(supu,0,(250,250,250))
                        screen.blit(supu,(70,265))
                        screen.blit(cont,(70,365))
                        pygame.display.flip()
                        print("su puntaje fue de: ",punt)
                        print("¿desea continuar? ")
                        restart=str(input())
                    if(restart=="no"):
                        screen.blit(clos,(70,165))
                        pygame.display.flip()
                        print("close")
pygame.quit()