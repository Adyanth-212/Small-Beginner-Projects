#!/usr/bin/python
import pygame
import time
import random
 
pygame.init()

#############
crash_sound = pygame.mixer.Sound("crash.wav")
#############
 
display_width = 800
display_height = 600
 
black = (0,0,0)
white = (255,255,255)

#Maximum value is 0 to 255
#     (r,  g, b)
red = (200,0,0)
green = (0,200,0)

bright_red = (255,0,0)
bright_green = (0,255,0)
 
block_color = (53,115,255)
 
 
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('DarkRacer')
clock = pygame.time.Clock()
 
carImg = pygame.image.load('racecar2.png')
gameIcon = pygame.image.load('racecar2.png')
imgx,imgy=carImg.get_rect().size
print(imgx,imgy)


car_width = imgx
max_x_width=display_width-car_width

pygame.display.set_icon(gameIcon)

pause = False
#crash = True
 
def things_dodged(count):
    font = pygame.font.SysFont("comicsansms", 25)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))
 
def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])
 
def car(x,y):
    gameDisplay.blit(carImg,(x,y))
 
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
 
 
def crash():
    ####################################
    pygame.mixer.Sound.play(crash_sound)
    pygame.mixer.music.stop()
    ####################################
    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects("You Crashed", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        

        button("Play Again",150,450,100,50,green,bright_green,game_loop)
        button("Quit",550,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15) 

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)
    

def quitgame():
    pygame.quit()
    quit()

def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause = False
    

def paused():
    ############
    pygame.mixer.music.pause()
    #############
    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        button("Continue",150,450,100,50,green,bright_green,unpause)
        button("Quit",550,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)   


def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)
        largeText = pygame.font.SysFont("comicsansms",115)
        TextSurf, TextRect = text_objects("Let's Race!", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("GO!",150,450,100,50,green,bright_green,game_loop)
        button("Quit",550,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)
        
        
    
    

    
def game_loop():
    global pause
    ############
    ############
    x = (display_width * 0.45)
    y = (display_height * 0.76)
 
    x_change = 0
 
    thing_width = 100
    thing_height = 100
    thing_startx = random.randrange(0, display_width-thing_width)
    thing_starty = -00
    thing_speed = 3
 
    thingCount = 1
    dodged = 0
    onhead_file="b4.wav"
    bkgnd_file="blksound.wav"


    if thing_speed >=4:
        onhead_file="b2.wav"

 
    pygame.mixer.music.load(bkgnd_file)
    pygame.mixer.music.play(-1)
    gameExit = False
 
    while not gameExit:
 
#        pygame.mixer.music.load('blksound.wav')
#        pygame.mixer.music.play(-1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -7
                    #print("DOWN_LEFT")
                if event.key == pygame.K_RIGHT:
                    #print("DOWN_RIGHT")
                    x_change = 7
                if event.key == pygame.K_p:
                    pause = True
                    paused()
                    
 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    print("UP_RIGHT")
                    x_change = 0

        if x>0 and (x< max_x_width):
            x+=x_change
        else:
            if x<=0:
                #pygame.mixer.music.stop()
                pygame.mixer.music.load('wall.wav')
                pygame.mixer.music.play(1)
                time.sleep(0.3)
                if x_change >0 :
                    x+=x_change
            elif x >= max_x_width:
                #pygame.mixer.music.stop()
                pygame.mixer.music.load('wall.wav')
                pygame.mixer.music.play(1)
                time.sleep(0.3)
                if x_change < 0:
                    x+=x_change



        gameDisplay.fill(white)
 
        things(thing_startx, thing_starty, thing_width, thing_height, block_color)
 
 
        
        thing_starty += thing_speed
        #print(x,y,thing_startx,thing_starty)
        car(x,y)
        #things_dodged(dodged)

        #AD Print to check if the block is falling on the head
        #tpos=thing_startx+(thing_width/2)
        #cpos=x+(car_width/2)
        #print(x,y,thing_startx,thing_starty)

        tx=thing_startx
        tw=thing_width
        cx=x
        cw=car_width

        print(tx,tw,cx,cw)
        if (tx > (cx+cw) ) or ((tx+tw)<cx):
            print("Not on Head")
            pygame.mixer.music.stop()
            pygame.mixer.music.load(bkgnd_file)
            pygame.mixer.music.play(-1)
        else:
            print ("1 Falling on head")
            pygame.mixer.music.stop()
            pygame.mixer.music.load(onhead_file)
            pygame.mixer.music.play(-1)

        #AD disable side crashes
        #if x > display_width - car_width or x < 0:
            #crash()
 
        if thing_starty > display_height:
            thing_starty = 0 
            #thing_startx = random.randrange(0,display_width-thing_width)
            thing_startx = random.randrange(x,x+100)
            dodged += 1
            #pygame.mixer.music.stop()
            #time.sleep(0.3)
            pygame.mixer.music.load('down.wav')
            pygame.mixer.music.play(1)
            #pygame.mixer.music.stop()
            time.sleep(0.3)
            pygame.mixer.music.load(bkgnd_file)
            pygame.mixer.music.play(-1)
            thing_speed = random.randrange(2,6)
            #thing_speed=3
            #thing_width += (dodged * 1.2)
            print("********************************Things speed =%d"%(thing_speed))
            onhead_file="b4.wav"
            if thing_speed >= 4:
                onhead_file="b2.wav"
 
        if y < thing_starty+thing_height:
            print('y crossover')
 
            if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx+thing_width:
                print('x crossover')
                crash()
        
        pygame.display.update()
        clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()
