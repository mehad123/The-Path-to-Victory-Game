# Game Name: The Path To Victory 
# Created by Mehad Ali 

#########################################################################

from pygame import *
init()
size = width, height = 1000, 700
screen = display.set_mode(size)

RED=(255,0,0)
GREY=(127,127,127)
BLACK=(0,0,0)
BLUE=(0,0,255)
GREEN=(0,255,0)
YELLOW=(255,255,0)
WHITE=(255,255,255)
ORANGE=(255,165,0)
PURPLE=(127,0,255)

mixer.music.load("songs/dbs.mp3")  #load a MUSIC object
mixer.music.play(-1) #Music clicked on is played indefinitely

Ground=650 #The ground for the game

jumpSpeed=-45 #Jump power
gravity=1.5 #Gravity
bottom=Ground #Bottom equals the ground

option1Rect=Rect(95,375,140,70) #'Start' rect object
option2Rect=Rect(20,475,330,70) #'Instructions' rect object
option3Rect=Rect(795,375,200,70)#'Credits' rect object

font1=font.SysFont("harrington",90,True) #Generating Harrington font
font2=font.SysFont("segoescript",50,True) #Generating Segoe Script font
font3=font.SysFont("inkfree",70,True) #Generating inkfree font
font4=font.SysFont("Comic Sans MS",20,True) #Generating Comic Sans MS font

singleRect=Rect(100,110,650,100) #Single player rect object
multiRect=Rect(420,510,560,100) #multiplayer rect object

character1=Rect(110,130,70,90) #Rect object for character 1 choice
character1M=Rect(110,450,70,90) #Rect object for character 1 choice for P2 to choose in multiplayer mode

character2=Rect(200,130,70,90) #Rect object for character 2 choice
character2M=Rect(200,450,70,90) #Rect object for character 2 choice for P2 to choose

character3=Rect(290,130,70,90) #Rect object for character 3 choice
character3M=Rect(290,450,70,90) #Rect object for character 3 choice for P2 to choose

### Player 1
p1x=0 #position for x-coord for player 1
p1y=1 #position for y-coord for player 1
p1w=2 # position for width of player 1
p1h=3 # position for height of player 1
p1Bot=2 #position of bottom of P1
p1v=[0,0,bottom] #velocity for P1
p1Rect=Rect(100,550,75,100)#Rect object for p1
p1Health=250 #Player 1's health

### Player 2
p2x=0 #position for x-coord for player 2
p2y=1 #position for y-coord for player 2
p2w=2 # position for width of player 2
p2h=3 # position for height of player 2
p2Bot=2 #position of bottom of P2
p2v=[0,0,bottom] #velocity for P2
p2Rect=Rect(800,550,75,100)#Rect object for p2
p2Health=250 #player 2's health

p1Choice=0 #P1 chooses a character (default is 0 - no character chosen)
p2Choice=0 #P2 chooses a character (default is 0 - no character chosen)

readyRect=Rect(750,315,180,60) #Rect object for "ready" button

moveP2=True #Player 2 CPU movement (in single player) is default always moving unless stated otherwise
hitP1=False #The default for P1 being hit is False, unless the other player attacks it -> this is triggered when 'v' is pressed in multiplayer and in single player, when cpu p2 collides with p1
hitP2=False #The default for P2 being hit is False, unless the other player attacks it ->this is triggered when 'm' is pressed by p1

kickP1=False #The default for P1 being hit is False, unless the other player attacks it -> this is triggered when 'b' is pressed in multiplayer and in single player, when cpu p2 collides
kickP2=False #The default for P2 being hit is False, unless the other player attacks it -> this is triggered when 'n' is pressed

damage=False #Default for damage is false unless the player is attacked

lvl1=image.load("images/lvl1.jpg").convert() #loads background image for lvl 1
background=image.load("images/dbzbackground.jpg").convert() #loads background image for start screen in menu
background2=image.load("images/dbzbackground2.jpg").convert() #loads background image for choosing player mode
chooseCharacter=image.load("images/chooseCharacter.jpg").convert() #loads background image for choosing character in single player
chooseCharacter2=image.load("images/chooseCharacter2.jpg").convert() #loads background image for choosing character in multiplayer
creditsPage=image.load("images/credits.png").convert() #loads background image for credits page

#Character option 1 sprites (loading images)
gokuStance=image.load("sprites/goku0.GIF").convert()
forwardGoku=image.load("sprites/goku1.GIF").convert()
backwardGoku=image.load("sprites/goku2.GIF").convert()
jumpGoku=image.load("sprites/goku3.GIF").convert()
punchGoku=image.load("sprites/goku4.GIF").convert()
kickGoku=image.load("sprites/goku5.GIF").convert()

#Character option 1 for P2 sprites (loading images)
gokuStance2=image.load("sprites/goku0M.GIF").convert()
forwardGoku2=image.load("sprites/goku1M.GIF").convert()
backwardGoku2=image.load("sprites/goku2M.GIF").convert()
jumpGoku2=image.load("sprites/goku3M.GIF").convert()
punchGoku2=image.load("sprites/goku4M.GIF").convert()
kickGoku2=image.load("sprites/goku5M.GIF").convert()

#Character option 2 sprites (loading images)
vegetaStance=image.load("sprites/vegeta0.GIF").convert()
forwardVegeta=image.load("sprites/vegeta1.GIF").convert()
backwardVegeta=image.load("sprites/vegeta2.GIF").convert()
jumpVegeta=image.load("sprites/vegeta3.GIF").convert()
punchVegeta=image.load("sprites/vegeta4.GIF").convert()
kickVegeta=image.load("sprites/vegeta5.GIF").convert()

#Character option 2 for P2 sprites (loading images)
vegetaStance2=image.load("sprites/vegeta0M.GIF").convert()
forwardVegeta2=image.load("sprites/vegeta1M.GIF").convert()
backwardVegeta2=image.load("sprites/vegeta2M.GIF").convert()
jumpVegeta2=image.load("sprites/vegeta3M.GIF").convert()
punchVegeta2=image.load("sprites/vegeta4M.GIF").convert()
kickVegeta2=image.load("sprites/vegeta5M.GIF").convert()

#Character option 3 sprites (loading images)
trunksStance=image.load("sprites/trunks0.GIF").convert()
forwardTrunks=image.load("sprites/trunks1.GIF").convert()
backwardTrunks=image.load("sprites/trunks2.GIF").convert()
jumpTrunks=image.load("sprites/trunks3.GIF").convert()
punchTrunks=image.load("sprites/trunks4.GIF").convert()
kickTrunks=image.load("sprites/trunks5.GIF").convert()

#Character option 3 for P2 sprites (loading images)
trunksStance2=image.load("sprites/trunks0M.GIF").convert()
forwardTrunks2=image.load("sprites/trunks1M.GIF").convert()
backwardTrunks2=image.load("sprites/trunks2M.GIF").convert()
jumpTrunks2=image.load("sprites/trunks3M.GIF").convert()
punchTrunks2=image.load("sprites/trunks4M.GIF").convert()
kickTrunks2=image.load("sprites/trunks5M.GIF").convert()

#Player 2 CPU sprites (loading images)
brolyStance=image.load("sprites/broly0.PNG").convert()
forwardBroly=image.load("sprites/broly1.PNG").convert()
backwardBroly=image.load("sprites/broly2.PNG").convert()
jumpBroly=image.load("sprites/broly3.PNG").convert()
kickBroly=image.load("sprites/broly4.PNG").convert()

mycounter=1 #counter variable for timing between the P2 CPU moving and attacking P1
myClock=time.Clock() 

stance=True #Stance (Or idle) -> Default is True, which tells whether or not P1 is standing still
stanceM=True #Stance (Or idle) 0-> Default is True, which tells whether or not P2 in multiplayer mode is standing still

def menu(action):
    'Function for menu screen of game'
    while action=="menu":
        for evnt in event.get():            
            if evnt.type == QUIT:
                action="end"
        
        screen.blit(background,(-50,0)) #outputs background
        
        mx,my=mouse.get_pos()
        mb=mouse.get_pressed()

        #Fonts for title
        title1=font1.render("Path To",True,WHITE)#Title font
        screen.blit(title1,(350,130)) #Blits part of the title
        title2=font1.render("Victory",True,WHITE)#Title font
        screen.blit(title2,(375,230)) #Blits the other part of the title

        #Fonts for options
        option1=font2.render("Start",True,WHITE)#First option font
        screen.blit(option1,(100,375)) #Blits the first option as "Start"
        draw.rect(screen,BLACK,option1Rect,4) #Rectangle object for Start button

        option2=font2.render("Instructions",True,WHITE) #2nd option font
        screen.blit(option2,(25,475)) #Blits the 2nd option as "Instructions"
        draw.rect(screen,BLACK,option2Rect,4) #Rect object for Instructions button

        option3=font2.render("Credits",True,WHITE) #3rd option font
        screen.blit(option3,(800,375)) #Blits 3rd option as "Credits"
        draw.rect(screen,BLACK,option3Rect,4) #Rect object for Credits button

        draw.rect(screen,BLACK,(5,645,580,40))#Draws a black rect around the line for the variable 'bacl'
        
        back=font4.render("To go back to any previous page, click the exit button",True,WHITE)
        screen.blit(back,(10,650)) #Blits the text

        if mb[0]==1: #If the left mouse is clicked
            if option1Rect.collidepoint(mx,my): #If the start button is clicked on
                play("play") #Transfers to the starting play screen
            if option2Rect.collidepoint(mx,my): #If the instructions button is clicked on
                instructions("instructions") #Transfers to the instructions screen
            if option3Rect.collidepoint(mx,my): #If the credits button is clicked on
                credits("credits") #Transfers to the credits screen
                
        display.flip()

def play(action):
    'Function for playing the game'
    while action=="play": #While the action is 'play'
        for evnt in event.get():            
            if evnt.type == QUIT: #If the close button is clicked
                action="end" #Goes back to the previous page
        
        screen.blit(background2,(0,0)) #outputs background

        draw.rect(screen,BLACK,singleRect) #Rect object for the single player button
        single=font1.render("Single Player",True,WHITE) #Single player font
        screen.blit(single,(100,100)) #Blits "single player"
        
        draw.rect(screen,BLACK,multiRect) #Rect object for the multiplayer button
        multi=font1.render("Multiplayer",True,WHITE) #Multiplayer font
        screen.blit(multi,(425,500)) #Blits "multiplayer"

        mx,my=mouse.get_pos()
        mb=mouse.get_pressed()

        if mb[0]==1: #if the left mouse is clicked
            if singleRect.collidepoint(mx,my): #If the single player button is clicked on
                singlePlayer("single") #Transfers to the choosing your character in single player mode
            if multiRect.collidepoint(mx,my): #If the multiplayer button is clicked
                multiplayer("multi") #Transfers to the choosing your character in multiplayer mode

        display.flip()

def singlePlayer(action):
    'Function for choosing your player in single player mode'

    ## Global variables ##
    global p1Health
    global p2Health
    global p1Rect
    global p2Rect
    
    global p1Choice
    global p2Choice
        
    p1Health=250 #Resets to 250 health after every round
    p2Health=250 #Resets to 250 health after every roumd
    p1Rect[p1x]=100 #Resets the position of p1 after every round
    p2Rect[p2x]=800 #Resets the position of p2 after every round

    while action=="single": #While the action is "single" player mode
        for evnt in event.get():
            if evnt.type==QUIT:
                return "endsingle" #If the exit button is pressed, it goes back to the previous page before
        
        screen.blit(chooseCharacter,(-10,0)) #outputs background

        chooseP1=font3.render("Player 1 - Choice",True,WHITE) #Player 1 Choice font
        screen.blit(chooseP1,(25,20)) #Blits title of that page

        draw.rect(screen,WHITE,character1) #Rect object for 1st character choice
        screen.blit(gokuStance,(120,130)) #Blits "Character 1" option

        draw.rect(screen,RED,character2) #Rect object for 2nd character choice
        screen.blit(vegetaStance,(210,130)) #Blits "Character 2" option

        draw.rect(screen,BLUE,character3) #Rect object for 3rd character choice
        screen.blit(trunksStance,(300,130)) #Blits "Character 3" option

        mx,my=mouse.get_pos()
        mb=mouse.get_pressed()

        if mb[0]==1: #If left mouse is clicked
            if character1.collidepoint(mx,my): #if character choice 1 is chosen
                p1Choice=1 #P1's choice is character 1
                levelS("levelS") #Switches to Single player level
            if character2.collidepoint(mx,my): #If character choice 2 is chosen
                p1Choice=2 #P1's choice is character 2
                levelS("levelS") #Switches to Single player level
            if character3.collidepoint(mx,my): #If character choice 3 is chosen
                p1Choice=3 #P1's choice is character 3
                levelS("levelS") #Switches to Single player level

        display.flip()

def levelS(action):
    'Function single player mode level'
    global p1Health
    global p2Health
    act="no action" #act is default set at 'no action'

    p1Health=250 #Resets to 250 health after every round
    p2Health=250 #Resets to 250 health after every roumd
    p1Rect[p1x]=100 #Resets the position of p1 after every round
    p2Rect[p2x]=800 #Resets the position of p2 after every round
    
    while action=="levelS": #While the action is in the single player level
        for evnt in event.get():
            if evnt.type==QUIT:
                return "endlevelS" #If the exit button is clicked, Single player level ends and goes back to the previous page
        p2Health=moveP1(p1Rect,p2Rect,p2Health) #fn that moves P1 and p2's health revolves around this function 
        checkP1(p1Rect) #fn that checks P1 is on ground

        p1Health=moveP2Single(p2Rect,p1Health) 
        checkP2Single(p1Rect) #fn that checks P2 is on ground

        p2Health=moveP1(p1Rect,p2Rect,p2Health) #fn 

        if p1Health<=0: #if p1's health is less than or equal zero
            act,p1Health,p2Health=gameOver("gameOver",p1Health,p2Health) #act switches to gameOver, p1 and p2's health is set to what gameOver's health is
        if p2Health<=0: #If p2's health is less than or equal to zero
            act,p1Health,p2Health=gameOver("gameOver",p1Health,p2Health) #act switches to gamveOver, p1 and p2's health is set to what gamOver's health is

        if act=="goback": #If the action is goback (because the button is pressed)
            return "endlevelS" #Screen switches back to previous page and ends single player level
        
        drawScene(p1Rect,p2Rect,p1Health,p2Health) #Draws the scene for lvl 1
        display.flip()

def drawScene(p1Rect,p2Rect,p1Health,p2Health):
    'Function for drawing the scenes in levels'
    keys=key.get_pressed()
      
    screen.blit(lvl1,(0,0)) #outputs background for level

    if p1Choice==1: #if p1's choice is character 1
        if keys[K_UP] or p1Rect[p1y]+p1Rect[p1h]>Ground: #if up arrow key is pressed and p1 is above the ground
            screen.blit(jumpGoku,(p1Rect[p1x],p1Rect[p1y])) #Blit the jumping sprite for character 1
        elif keys[K_RIGHT]:#if right arrow key is pressed
            screen.blit(forwardGoku,(p1Rect[p1x],p1Rect[p1y])) #Blit the going forward sprite for character 1
        elif keys[K_LEFT]:#if left arrow key is pressed
            screen.blit(backwardGoku,(p1Rect[p1x],p1Rect[p1y])) #Blit the going backward sprite for character 1
        elif keys[K_m]: #if the 'm' key is pressed
            screen.blit(punchGoku,(p1Rect[p1x],p1Rect[p1y])) #Blit the punching sprite for character 1
        elif keys[K_n]: #if the 'n' key is pressed
            screen.blit(kickGoku,(p1Rect[p1x],p1Rect[p1y])) #Blit the kicking sprite for character 1
        else: #if none of the buttons above were pressed
            screen.blit(gokuStance,(p1Rect[p1x],p1Rect[p1y])) ##Blit the standing sprite for character 1

    elif p1Choice==2: # Same as above except character 2 was chosen -> so different sprites 
        if keys[K_UP] or p1Rect[p1y]+p1Rect[p1h]>Ground:
            screen.blit(jumpVegeta,(p1Rect[p1x],p1Rect[p1y]))             
        elif keys[K_RIGHT]:
            screen.blit(forwardVegeta,(p1Rect[p1x],p1Rect[p1y]))
        elif keys[K_LEFT]:
            screen.blit(backwardVegeta,(p1Rect[p1x],p1Rect[p1y]))
        elif keys[K_m]:
            screen.blit(punchVegeta,(p1Rect[p1x],p1Rect[p1y]))
        elif keys[K_n]:
            screen.blit(kickVegeta,(p1Rect[p1x],p1Rect[p1y]))
        else:
            screen.blit(vegetaStance,(p1Rect[p1x],p1Rect[p1y]))

    elif p1Choice==3: # Same as above except character 3 was chosen -> so different sprites
        if keys[K_UP] or p1Rect[p1y]+p1Rect[p1h]>Ground:
            screen.blit(jumpTrunks,(p1Rect[p1x],p1Rect[p1y]))
        elif keys[K_RIGHT]:
            screen.blit(forwardTrunks,(p1Rect[p1x],p1Rect[p1y]))            
        elif keys[K_LEFT]:
            screen.blit(backwardTrunks,(p1Rect[p1x],p1Rect[p1y]))
        elif keys[K_m]:
            screen.blit(punchTrunks,(p1Rect[p1x],p1Rect[p1y]))
        elif keys[K_n]:
            screen.blit(kickTrunks,(p1Rect[p1x],p1Rect[p1y]))
        else:
            screen.blit(trunksStance,(p1Rect[p1x],p1Rect[p1y]))

    ## CPU player 2 ##
    if p1Rect[p1y]+140<p2Rect[p2y]: #If p1's height is greater than p2's y-coord
        if p2Rect[p2y]+p2Rect[p2h]==p2v[p2Bot] and p2v[p2y]==0: 
            screen.blit(jumpBroly,(p2Rect[p2x],p2Rect[p2y]-20)) #Blits the jumping sprite for p2
    if p1Rect[p1x]>p2Rect[p2x]+80: #if player 1's x-coord is greater than player 2's x-coord
        screen.blit(backwardBroly,(p2Rect[p2x],p2Rect[p2y]-20)) #Blits the moving backward sprite for p2
    elif p1Rect[p1x]+85<p2Rect[p2x]:#if player 1's x-coord (+width) is less than p2's x-coord
        screen.blit(forwardBroly,(p2Rect[p2x],p2Rect[p2y]-20)) #Blits the moving forward sprite for p2
    elif p2Rect.colliderect(p1Rect): #If p2 collides with p1
        screen.blit(kickBroly,(p2Rect[p2x],p2Rect[p2y]-20)) #Blits the kicking sprite for p2
    else: #If none of these actions are happening
        screen.blit(brolyStance,(p2Rect[p2x],p2Rect[p2y]-20)) #blits the regular stance of p2
        
    draw.rect(screen,RED,(150,50,p1Health,20)) #Draws p1's health bar at the top
    draw.rect(screen,RED,(600,50,p2Health,20)) #Draws p2's health bar at the top
    
    display.flip()

def moveP1(p1Rect,p2Rect,p2Health):
    'moving player 1'
    keys=key.get_pressed()
    global stance
    stance=False #Default stance is false
    hitP2=False
    kickP2=False
    
    if p1Choice==1: #if p1's choice is character 1
        if keys[K_UP] and p1Rect[p1y]+p1Rect[p1h]==p1v[p1Bot] and p1v[p1y]==0:
            p1v[p1y]=jumpSpeed #P1's velocity y-coord is the jumpspeed
            
        elif keys[K_RIGHT]:#if right arrow key is pressed
            p1v[p1x]=2 #Player 1 moves to the right
            
        elif keys[K_LEFT]:#if left arrow key is pressed
            p1v[p1x]=-2 #Player 1 moves to the left
        elif keys[K_m]: #If the 'm' button is clicked
            hitP2=True #hitting p2 is true
        elif keys[K_n]: #if the 'n' button is clicked
            kickP2=True #kicking p2 is true
        else: #If none of these buttons are pressed
            p1v[p1x]=0 #P1 doesn't move
            hitP2=False #hitting p2 is false
            kickP2=False #kicking p2 is false
            stance=True #Standing still is True
    
    elif p1Choice==2: ## Same as above except character 2 was chosen ##
        if keys[K_UP] and p1Rect[p1y]+p1Rect[p1h]==p1v[p1Bot] and p1v[p1y]==0:
            p1v[p1y]=jumpSpeed
            
        if keys[K_RIGHT]:#if right arrow key is pressed
            p1v[p1x]=2 #Player 1 moves to the right
            
        elif keys[K_LEFT]:#if left arrow key is pressed
            p1v[p1x]=-2 #Player 1 moves to the left
        elif keys[K_m]:
            hitP2=True
        elif keys[K_n]:
            kickP2=True
        else:
            p1v[p1x]=0
            hitP2=False
            kickP2=False
            stance=True
            
    elif p1Choice==3: ## Same as above except character 3 was chosen ##
        if keys[K_UP] and p1Rect[p1y]+p1Rect[p1h]==p1v[p1Bot] and p1v[p1y]==0:
            p1v[p1y]=jumpSpeed
            
        if keys[K_RIGHT]:#if right arrow key is pressed
            p1v[p1x]=2 #Player 1 moves to the right
            
        elif keys[K_LEFT]:#if left arrow key is pressed
            p1v[p1x]=-2 #Player 1 moves to the left
        elif keys[K_m]:
            hitP2=True
        elif keys[K_n]:
            kickP2=True
        else:
            p1v[p1x]=0
            hitP2=False
            kickP2=False
            stance=True
        
    p1Rect[p1x]+=p1v[p1x] #Moves P2
    p1v[p1y]+=gravity 

    if p1Rect[p1x]<=0:#Player 1 cant go out of screen
        p1Rect[p1x]=0
    if p1Rect[p1x]+75>width: #Player 1 cant go out of screen
        p1Rect[p1x]=925

    if p1Rect.colliderect(p2Rect) and hitP2==True: #If p1 collides with p2 and 'm' was pressed
        p2Health-=25 #P2's health bar goes down by 25
        p2Rect[p2x]+=100 #p2 is pushed back
        
    elif p1Rect.colliderect(p2Rect) and kickP2==True: #If p1 collides with p2 and 'n' was pressed
        p2Health-=25 #P2's health bar goes down by 25 
        p2Rect[p2x]+=100 #p2 is pushed back
        
    return p2Health #Returns p2's health
            
def moveP2Single(p2Rect,p1Health):
    'moving CPU player 2 in single player mode'
    global mycounter
    global damage

    if mycounter%300==0: #If 5 seconds have passed
       damage=True
       moveP2=True

    if p1Rect[p1y]+140<p2Rect[p2y]: #If p1's height is greater than p2's y coord
        if p2Rect[p2y]+p2Rect[p2h]==p2v[p2Bot] and p2v[p2y]==0:
            p2v[p2y]=jumpSpeed #p2's velocity y-coord equals the jumpspeed
            moveP2=True #P2 movement is true
    if p1Rect[p1x]>p2Rect[p2x]+80: #if player 1's x-coord is greater than player 2's x-coord
        p2v[p2x]=2 #Player 2 moves right
        moveP2=True #P2 movement is true
    elif p1Rect[p1x]+85<p2Rect[p2x]:#if player 1's x-coord (+width) is less than p2's x-coord
        p2v[p2x]=-2 #player 2 moves left
        moveP2=True #P2 movement is true
    else: #if none of those actions happen
        p2v[p2x]=0 #P2 is standing still
        moveP2=False #p2 is currently not moving -> False

    if p2Rect[p2x]<=0:#Player 1 cant go out of screen
        p2Rect[p2x]=0
    if p2Rect[p2x]+75>width: #Player 1 cant go out of screen
        p2Rect[p2x]=925

    if p2Rect.colliderect(p1Rect) and damage==True and mycounter>60: #if p2 collides with p1 and damaging is true and 60 frames have passed
        p1Health-=25 #P1's health bar goes down by 25
        moveP2=False #P2's movement is false
        p1Rect[p1x]-=100 #P1 is pushed back
        mycounter=1 #mycounter resets back to 1

    p2Rect[p2x]+=p2v[p2x] #P2 moves
    p2v[p2y]+=gravity
    
    mycounter+=1 #mycounter increases by 1
    return p1Health #Returns p1's health

def checkP1(p1Rect): 
    'Checks to make sure P1 doest go through the ground'
    p1Rect[p1y]+=p1v[p1y] #p1's y-coord adds on p1's velocity y-coord
    if p1Rect[p1y]+p1Rect[p1h]>=Ground: #if p1's height is greater than or equal to the ground
        p1v[p1Bot]=Ground 
        p1Rect[p1y]=Ground-p1Rect[p1h]
        p1v[p1y]=0

def checkP2Single(p2Rect):
    'Checks to make sure P2 doesnt go through the ground'
    p2Rect[p2y]+=p2v[p2y] #p1's y-coord adds on p1's velocity y-coord
    if p2Rect[p2y]+p2Rect[p2h]>=Ground:#if p1's height is greater than or equal to the ground
        p2v[p2Bot]=Ground
        p2Rect[p2y]=Ground-p2Rect[p2h]
        p2v[p2y]=0

def gameOver(action,p1Health,p2Health):
    'Game over screen after either players health reachers zero'
    while action=="gameOver": #While the action is gameOver
        for evnt in event.get():
            if evnt.type==QUIT: #if the exit button is pressed
                return "goback",250,250 #Goes back to the choosing characters page, p1 and p2's health reset back to 250
                
        screen.fill(BLACK) #Screen color is black

        if p1Health<=0: #If p1's health is less than or equal to zero
            gameOverFont=font1.render("Player 2 Wins", True, WHITE)
            screen.blit(gameOverFont,(250,250)) #Blits the text of p2 winning
        if p2Health<=0: #If p2's health is less than or equal to zero
            gameOverFont=font1.render("Player 1 Wins", True, WHITE) 
            screen.blit(gameOverFont,(250,250)) #blits the text of p1 winning

        playAgainRect=Rect(395,415,400,100) #Rect object for playing again
        draw.rect(screen,WHITE,playAgainRect,5) #Draws the rect object
        playAgainFont=font3.render("Play Again",True,WHITE)
        screen.blit(playAgainFont,(400,420)) #Blits the text of playing again

        mx,my=mouse.get_pos()
        mb=mouse.get_pressed()

        if playAgainRect.collidepoint(mx,my) and mb[0]==1: #If mouse clicks on the play again button
            return "goback",250,250 #Switches to choosing character screen to play again

        display.flip()
    return"goback",p1Health,p2Health #Returns going back to the choosing character screen

def multiplayer(action):
    'Function for choosing characters in multiplayer mode'
    global p1Health
    global p2Health
    global p1Rect
    global p2Rect

    global p1Choice
    global p2Choice
    
    p1Health=250 #Resets to 250 health after every round
    p2Health=250 #Resets to 250 health after every roumd
    p1Rect[p1x]=100 #Resets the position of p1 after every round
    p2Rect[p2x]=800 #Resets the position of p2 after every round
    
    p1Chosen=False #No character has been selected for P1 (default is False)
    p2Chosen=False #No character has been selected for P2 (default is False)
    while action=="multi": #While the action is multiplayer
        for evnt in event.get():
            if evnt.type==QUIT: #If the exit button is pressed 
                action="end" #Goes back to the previous page
        
        screen.blit(chooseCharacter2,(0,0)) #outputs background

        chooseP1=font3.render("Player 1 - Choice",True,WHITE) #P1 Choice font
        screen.blit(chooseP1,(25,20)) #Blits title of that page

        chooseP2=font3.render("Player 2 - Choice",True,WHITE) #P2 Choice font
        screen.blit(chooseP2,(25,350)) #Blits title of that page

        draw.rect(screen,WHITE,readyRect) #Rect object for "Ready"
        draw.rect(screen,GREEN,readyRect,10) #Rect object outline for "Ready"
        readyFont=font2.render("Ready",True,BLACK) #Ready font
        screen.blit(readyFont,(755,305)) #Blits 'Ready'

        p1Left=font4.render("Left-click to choose",True,WHITE) #p1Left font
        p2Right=font4.render("Right-click to choose",True,WHITE) #p2Right font
        screen.blit(p1Left,(180,90)) #Blits "left-click to choose"
        screen.blit(p2Right,(180,420))#Blits 'right-click to choose'

        draw.rect(screen,WHITE,character1) #Rect object for 1st character choice
        screen.blit(gokuStance,(120,130))

        draw.rect(screen,RED,character2) #Rect object for 2nd character choice
        screen.blit(vegetaStance,(210,130))

        draw.rect(screen,BLUE,character3) #Rect object for 3rd character choice
        screen.blit(trunksStance,(300,130))

        draw.rect(screen,WHITE,character1M) #Draws 1st character choice box for P2
        screen.blit(gokuStance2,(110,450))

        draw.rect(screen,RED,character2M) #Rect object for 2nd character choice for P2
        screen.blit(vegetaStance2,(200,450))

        draw.rect(screen,BLUE,character3M) #Rect object for 3rd character choice for P2
        screen.blit(trunksStance2,(290,450))
        
        mx,my=mouse.get_pos()
        mb=mouse.get_pressed()

        if mb[0]==1: #If the mouse button is left-clicked
            if character1.collidepoint(mx,my): #If the mouse clicks on the character 1 box choice
                p1Choice=1 #P1's choice is character 1
                p1Chosen=True #P1 has chosen, so therefore its true
            if character2.collidepoint(mx,my): #If the mouse clicks on the character 2 box choice
                p1Choice=2 #P1's choice is character 2
                p1Chosen=True #P1 has chosen, so therefore its true
            if character3.collidepoint(mx,my): #If the mouse clicks on the character 3 box choice
                p1Choice=3 #P1's choice is character 3
                p1Chosen=True #P1 has chosen, so therefore its true
        if mb[2]==1: #If the mouse button is right-clicked
            if character1M.collidepoint(mx,my): #if the mouse clicks on the character 1 box choice for p2
                p2Choice=1 #P2's choice is character 1
                p2Chosen=True #P2 has chosen, so therefore its true
            if character2M.collidepoint(mx,my): #if the mouse clicks on the character 2 box choice for p2
                p2Choice=2 #P2's choice is character 2
                p2Chosen=True #P2 has chosen, so therefore its true
            if character3M.collidepoint(mx,my): #if the mouse clicks on the character 3 box choice for p2
                p2Choice=3 #P2's choice is character 3
                p2Chosen=True #P2 has chosen, so therefore its true
        if p1Chosen==True and p2Chosen==True: #If P1 and P2's choices have been chosen (true)
            if mb[0]==1 and readyRect.collidepoint(mx,my): #If the mouse clicks on the ready button..
                levelM("levelM") #Screen switchs to the multiplayer levels

        display.flip()

def levelM(action):
    'Function for multiplayer mode levels'
    global p1Health
    global p2Health
    act="no action"
    p1Rect[p1x]=100
    p2Rect[p2x]=800
    
    while action=="levelM": #While the action is multiplayer level
        for evnt in event.get():
            if evnt.type==QUIT: #If the exit button is pressed
                action="endlevelM" #Goes back to the previous page before
        p2Health=moveP1(p1Rect,p2Rect,p2Health) #fn that moves P1 and p2's health revolves around this function
        checkP1(p1Rect) #fn that checks if p1 is on the ground
        
        p1Health=moveP2Multi(p2Rect,p1Rect,p1Health) #fn that moves P2 in multiplayer mode and p1's health revolves around this fn
        checkP2Multi(p2Rect) #fn that checks if p2 is on the ground

        p2Health=moveP1(p1Rect,p2Rect,p2Health) #Its the same fn as above, but for some reason it helps slow down the jumping -> so i kept it
        p1Health=moveP2Multi(p2Rect,p1Rect,p1Health) #Its the same fn as above, but for some reason it helps slow down the jumping -> so i kept it

        if p1Health<=0: #if p1's health is less than or equal zero
            act,p1Health,p2Health=gameOver("gameOver",p1Health,p2Health) #act switches to gameOver, p1 and p2's health is set to what gameOver's health is
        if p2Health<=0: #If p2's health is less than or equal to zero
            act,p1Health,p2Health=gameOver("gameOver",p1Health,p2Health) #act switches to gamveOver, p1 and p2's health is set to what gamOver's health is

        if act=="goback": #If the action is goback (because the button is pressed)
            return "endlevelM" #Screen switches back to previous page and ends multiplayer level
        
        drawSceneMulti(p1Rect,p2Rect,p1Health,p2Health) #fn that draws the screen in multiplayer mode
        display.flip()

def drawSceneMulti(p1Rect,p2Rect,p1Health,p2Health):
    'Function for drawing the scenes in levels'
    keys=key.get_pressed()
    screen.blit(lvl1,(0,0)) #outputs background for multiplayer level

##   Player 1   ##
    if p1Choice==1: #If p2's choice was character 1
        if keys[K_UP] or p1Rect[p1y]+p1Rect[p1h]>Ground: #if up arrow key was pressed and p1's height was above ground
            screen.blit(jumpGoku,(p1Rect[p1x],p1Rect[p1y])) #blits the jumping sprite for char 1
        elif keys[K_RIGHT]:#if right arrow key is pressed 
            screen.blit(forwardGoku,(p1Rect[p1x],p1Rect[p1y])) #blits the moving forward sprite for char 1        
        elif keys[K_LEFT]:#if left arrow key is pressed
            screen.blit(backwardGoku,(p1Rect[p1x],p1Rect[p1y])) #blits the moving backward sprite for char 1
        elif keys[K_m]: #If 'm' key is pressed
            screen.blit(punchGoku,(p1Rect[p1x],p1Rect[p1y])) #blits the punching sprite for char 1
        elif keys[K_n]: #if 'n' key is pressed
            screen.blit(kickGoku,(p1Rect[p1x],p1Rect[p1y])) #blits the kicking sprite for char 1
        else: #If none of the keys above were pressed
            screen.blit(gokuStance,(p1Rect[p1x],p1Rect[p1y])) #Blits the default stance sprite for char 1

    elif p1Choice==2: ## Same as above except char 2 was chosen ##
        if keys[K_UP] or p1Rect[p1y]+p1Rect[p1h]>Ground:
            screen.blit(jumpVegeta,(p1Rect[p1x],p1Rect[p1y]))             
        elif keys[K_RIGHT]:
            screen.blit(forwardVegeta,(p1Rect[p1x],p1Rect[p1y]))
        elif keys[K_LEFT]:
            screen.blit(backwardVegeta,(p1Rect[p1x],p1Rect[p1y]))
        elif keys[K_m]:
            screen.blit(punchVegeta,(p1Rect[p1x],p1Rect[p1y]))
        elif keys[K_n]:
            screen.blit(kickVegeta,(p1Rect[p1x],p1Rect[p1y]))
        else:
            screen.blit(vegetaStance,(p1Rect[p1x],p1Rect[p1y]))

    elif p1Choice==3: ## Same as above except char 3 was chosen
        if keys[K_UP] or p1Rect[p1y]+p1Rect[p1h]>Ground:
            screen.blit(jumpTrunks,(p1Rect[p1x],p1Rect[p1y]))
        elif keys[K_RIGHT]:
            screen.blit(forwardTrunks,(p1Rect[p1x],p1Rect[p1y]))            
        elif keys[K_LEFT]:
            screen.blit(backwardTrunks,(p1Rect[p1x],p1Rect[p1y]))
        elif keys[K_m]:
            screen.blit(punchTrunks,(p1Rect[p1x],p1Rect[p1y]))
        elif keys[K_n]:
            screen.blit(kickTrunks,(p1Rect[p1x],p1Rect[p1y]))
        else:
            screen.blit(trunksStance,(p1Rect[p1x],p1Rect[p1y]))

##   Player 2 Multiplayer ##    
    if p2Choice==1: # Same concept as above except its p2's choice and the sprites are flipped
        if keys[K_w] or p2Rect[p2y]+p2Rect[p2h]>Ground: #if 'w' key was pressed and p2's height was above ground
            screen.blit(jumpGoku2,(p2Rect[p2x],p2Rect[p2y]))            
        elif keys[K_d]:#if 'd' key is pressed
            screen.blit(backwardGoku2,(p2Rect[p2x],p2Rect[p2y]))            
        elif keys[K_a]:#if 'a' key was pressed
            screen.blit(forwardGoku2,(p2Rect[p2x],p2Rect[p2y]))
        elif keys[K_v]: #If 'v' was pressed -> punching button
            screen.blit(punchGoku2,(p2Rect[p2x],p2Rect[p2y]))
        elif keys[K_b]: #if 'b' was pressed -> kicking button
            screen.blit(kickGoku2,(p2Rect[p2x],p2Rect[p2y]))
        else: #if none of the keys above were pressed
            screen.blit(gokuStance2,(p2Rect[p2x],p2Rect[p2y]))
        
    elif p2Choice==2: # Same as above except char 2 was chosen by p2
        if keys[K_w] or p2Rect[p2y]+p2Rect[p2h]>Ground:
            screen.blit(jumpVegeta2,(p2Rect[p2x],p2Rect[p2y]))
        elif keys[K_d]:
            screen.blit(backwardVegeta2,(p2Rect[p2x],p2Rect[p2y]))            
        elif keys[K_a]:
            screen.blit(forwardVegeta2,(p2Rect[p2x],p2Rect[p2y]))
        elif keys[K_v]:
            screen.blit(punchVegeta2,(p2Rect[p2x],p2Rect[p2y]))
        elif keys[K_b]:
            screen.blit(kickVegeta2,(p2Rect[p2x],p2Rect[p2y]))
        else:
            screen.blit(vegetaStance2,(p2Rect[p2x],p2Rect[p2y]))
        
    elif p2Choice==3: # Same as above except char 2 was chosen by p2
        if keys[K_w] or p2Rect[p2y]+p2Rect[p2h]>Ground:
            screen.blit(jumpTrunks2,(p2Rect[p2x],p2Rect[p2y]))
        elif keys[K_d]:
            screen.blit(backwardTrunks2,(p2Rect[p2x],p2Rect[p2y]))            
        elif keys[K_a]:
            screen.blit(forwardTrunks2,(p2Rect[p2x],p2Rect[p2y]))
        elif keys[K_v]:
            screen.blit(punchTrunks2,(p2Rect[p2x],p2Rect[p2y]))
        elif keys[K_b]:
            screen.blit(kickTrunks2,(p2Rect[p2x],p2Rect[p2y]))
        else:
            screen.blit(trunksStance2,(p2Rect[p2x],p2Rect[p2y]))
        
    draw.rect(screen,RED,(150,50,p1Health,20)) #Draws p1's health bar
    draw.rect(screen,RED,(600,50,p2Health,20)) #Draws p2's health bar
    
    display.flip()


def moveP2Multi(p2Rect,p1Rect,p1Health): 
    'moving player 2 in multiplayer mode'
    keys=key.get_pressed()
    global stanceM
    stanceM=False
    hitP1=False
    kickP1=False
    
    if p2Choice==1:
        if keys[K_w] and p2Rect[p2y]+p2Rect[p2h]==p2v[p2Bot] and p2v[p2y]==0: #if 'w' was pressed 
            p2v[p2y]=jumpSpeed
            
        if keys[K_d]:#if 'd' key is pressed
            p2v[p2x]=2 #Player 2 moves to the right
            
        elif keys[K_a]:#if 'a' key is pressed
            p2v[p2x]=-2 #Player 2 moves to the left
        elif keys[K_v]: #If 'v' was pressed
            hitP1=True #hitting p1 is true
        elif keys[K_b]: #if 'b' is pressed
            kickP1=True #kicking p1 is true
        else: #if none of the keys above were pressed
            p2v[p1x]=0 #P2 is standing still
            hitP1=False #hitting p1 is false
            kickP1=False #kicking p1 is false
            stanceM=True #Stance is true -> p2 is standing still
            
    elif p2Choice==2: #Same as above except its char 2
        if keys[K_w] and p2Rect[p2y]+p2Rect[p2h]==p2v[p2Bot] and p2v[p2y]==0:
            p2v[p2y]=jumpSpeed 
        if keys[K_d]:
            p2v[p2x]=2 
            
        elif keys[K_a]:
            p2v[p2x]=-2 
        elif keys[K_v]:
            hitP1=True
        elif keys[K_b]:
            kickP1=True
        else:
            p2v[p1x]=0
            hitP1=False
            kickP1=False
            stanceM=True
            
    elif p2Choice==3: # Same as above except its char 3
        if keys[K_w] and p2Rect[p2y]+p2Rect[p2h]==p2v[p2Bot] and p2v[p2y]==0:
            p2v[p2y]=jumpSpeed 
        if keys[K_d]:
            p2v[p2x]=2 
            
        elif keys[K_a]:
            p2v[p2x]=-2 
        elif keys[K_v]:
            hitP1=True
        elif keys[K_b]:
            kickP1=True
        else:
            p2v[p1x]=0
            hitP1=False
            kickP1=False
            stanceM=True
            
    p2Rect[p2x]+=p2v[p1x] #Moves P2
    p2v[p2y]+=gravity

    if p2Rect.colliderect(p1Rect) and hitP1==True: #If p2 collides with p1 and 'v' is pressed
        p1Health-=25 #P1's health goes down by 25
        p1Rect[p1x]-=100 #p1 is pushed back
        
    if p2Rect.colliderect(p1Rect) and kickP1==True: #if p2 collides with p1 and 'b' is pressed
        p1Health-=25 #P2's health goes down by 25
        p1Rect[p1x]-=100 #p2 is pushed back

    if p2Rect[p2x]<=0:#Player 2 cant go out of screen
        p2Rect[p2x]=0 
    elif p2Rect[p2x]+75>width: #Player 2 cant go out of screen
        p2Rect[p2x]=925

    display.flip()
    return p1Health #returns p1's health

def checkP2Multi(p2Rect):
    'checks to make sure that P2 doesnt fall thru the ground'
    p2Rect[p2y]+=p2v[p2y]
    if p2Rect[p2y]+p2Rect[p2h]>=Ground: #if p2's height is greater than or equal to the ground
        p2v[p2Bot]=Ground
        p2Rect[p2y]=Ground-p2Rect[p2h]
        p2v[p2y]=0

def instructions(action): #Function for the instructions of the game
    while action=="instructions":
        for evnt in event.get():            
            if evnt.type == QUIT: #if exit button is pressed
                action="end" #Goes back to previous page (menu)
        
        screen.blit(background,(-50,0)) #outputs background

        instruct=font3.render("Instructions",True,WHITE) #Instructions font
        screen.blit(instruct,(300,105)) #Blits "Instructions"

        draw.rect(screen,BLACK,(40,190,920,270)) #Draws a black rectangle behind the text

        player1=font2.render("Player 1",True,WHITE)
        screen.blit(player1,(80,200))

        dashes1=font2.render("-------",True,WHITE)
        screen.blit(dashes1,(80,230))

        line1=font4.render("Right & Left Arrow Keys To Move",True,WHITE)
        screen.blit(line1,(50,300))

        line2=font4.render("Up Arrow Key To Jump",True,WHITE)
        screen.blit(line2,(50,350))

        line3=font4.render("'m' & 'n' To Attack",True,WHITE)
        screen.blit(line3,(50,400))

        player2=font2.render("Player 2",True,WHITE)
        screen.blit(player2,(700,200))
    
        dashes2=font2.render("-------",True,WHITE)
        screen.blit(dashes2,(700,230))

        line4=font4.render("'a' & 'd' To Move",True,WHITE)
        screen.blit(line4,(680,300))

        line5=font4.render("'w' To Jump",True,WHITE)
        screen.blit(line5,(680,350))
        
        line6=font4.render("'v' & 'b' To Attack",True,WHITE)
        screen.blit(line6,(680,400))
        
        display.flip()

def credits(action): #Function for the credits
    while action=="credits":
        for evnt in event.get():            
            if evnt.type == QUIT: #if exit button is pressed
                action="end" #Goes back to previous page (menu)
        
        screen.blit(creditsPage,(0,0)) #outputs background

        mehad=font3.render("Created by Mehad Ali",True,WHITE)
        screen.blit(mehad,(20,250))

        dashes3=font2.render("------------------------",True,WHITE)
        screen.blit(dashes3,(20,290))

        based=font2.render("Based Off Of The DBS Anime",True,WHITE)
        screen.blit(based,(20,350))
        
        display.flip()

###MAIN PROGRAM
menu("menu")
quit()
