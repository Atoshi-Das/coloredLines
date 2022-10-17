#importing the library
import pygame
import random as r



#initialising pygame
pygame.init()
#RGB color
LightGrey = (211,211,211)
red = (255,0,0)
blue = (0,0,255)
dark_pink = (231,84,128)
yellow = (255,255,0)
green = (0,255,0)
violet = (148,0,211)



#initialising screen
screen = pygame.display.set_mode((650,650))
screen.fill(LightGrey)
pygame.display.update()




#Randomly importing the balls
# function call-> random_balls()
c = [(r.randrange(0,540,60) + 30, r.randrange(0,540,60) + 30)]
# c = coordinates
def random_balls(c):
    
    print(r.choice(c))
    count = 1
#6 colors importing to grid
    while count != 8:
        x = r.randrange(0,540,60)
        y = r.randrange(0,540,60)
        if (x, y) not in c: #x and y are coordinates
            c.append((x + 30, y + 30))

            count += 1
        print(c)
    circle = pygame.draw.circle(screen,(red), c[0],(22))      #red
    circle = pygame.draw.circle(screen,(blue),c[1],(22))      #blue
    circle = pygame.draw.circle(screen,(dark_pink),c[2],(22)) #dark pink
    circle = pygame.draw.circle(screen,(yellow),c[3],(22))    #yellow
    circle = pygame.draw.circle(screen,(green),c[4],(22))     #green
    circle = pygame.draw.circle(screen,(red),(c[5]),(22))     #red
    circle = pygame.draw.circle(screen,(violet),c[6],(22))    #violet
    circle = pygame.draw.circle(screen,(blue),c[7],(22))      #blue

    

    
'''#clicking the ball and replacing the place
def click():
    #x,y = pygame.mouse.get_pos()
    mouse = pygame.mouse.get_pressed()
    #print(mouse)
    #Balls(c)
    if pygame.mouse.get_pressed():
        if Balls(c) == mouse:
            d = Balls(c)
            mouse = pygame.draw.circle(screen,(211,211,211),(22))#Light Grey
            pygame.display.update()
            print(d)
        if mouse == True:
             x1,y1 = pygame.mouse.get_pos()
             print(d)
             pygame.display.update()'''
        
         
        
    
        
        
        

#3 colors importing to grid after the movement
'''def ball(c1):
    print(r.choice(c1))
    c1 = [(r.randrange(0,540,60) + 30, r.randrange(0,540,60) + 30)]
    
    count = 1

    
    while count != 4:
        x2 = r.randrange(0,540,60)
        y2 = r.randrange(0,540,60)
        if (x1,y1) not in Balls(c):
           c.append((x2 + 30,y2 + 30))
           count += 1
    print(c)
    circle = pygame.draw.circle(screen,(255,0,0), c[0],(22))#red
    circle = pygame.draw.circle(screen,(0,0,255),c[1],(22))#blue
    circle = pygame.draw.circle(screen,(231,84,128),c[2],(22))#dark pink
    circle = pygame.draw.circle(screen,(255,255,0),c[3],(22))#yellow
    circle = pygame.draw.circle(screen,(0,255,0),c[4],(22))#green
    
    circle = pygame.draw.circle(screen,(148,0,211),c[6],(22))#violet'''







#displaying title and icon
pygame.display.set_caption("COLORED LINES")
random_balls(c)
#click()



#Drawing horizontal lines
y = 60
for i in range(9):
    pygame.draw.line(screen,(0,0,0),(0,y),(540,y))
    y += 60

    
#Drawing vertical lines
x = 60
for i in range(9):
    pygame.draw.line(screen,(0,0,0),(x,0),(x,540))
    x += 60
   
pygame.display.update()





#Quiting the game
while True:
    #considering the variables
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            
            #for closing the window
            run = False



    
                
pygame.display.update()
   

pygame.quit()
