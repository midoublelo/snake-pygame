import pygame
import time
import random
# from sense_hat import SenseHat

# sense = SenseHat()
 
pygame.init()
 
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
grey = (200, 200, 200)
grey2 = (150, 150, 150)
 
windowWidth = 600
windowHeight = 400

# pygame.mixer.init
# appleSound = pygame.mixer.music.load("apple.ogg")
# lemonSound = pygame.mixer.music.load("lemon.ogg")
 
display = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("Snake in Pygame")
 
timer = pygame.time.Clock()
 
snakeBlock = 10
snakeSpeed = 10
 
fontStyle = pygame.font.SysFont("linuxlibertineo", 25)
scoreFont = pygame.font.SysFont("linuxlibertineo", 35)

# sense.clear(grey)

def playerScore(score):
    value = scoreFont.render("Your Score: " + str(score), True, black)
    display.blit(value, [0, 0])
 
def playerSnake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, green, [x[0], x[1], snakeBlock, snakeBlock])
 
def message(msg, color):
    mesg = fontStyle.render(msg, True, color)
    display.blit(mesg, [windowWidth / 6, windowHeight / 3])
 
def gameLoop():
    gameOver = False
    gameClose = False
 
    x1 = windowWidth / 2
    y1 = windowHeight / 2
 
    x1_change = 0
    y1_change = 0
 
    snakeList = []
    snakeLength = 1
 
    appleXPos = round(random.randrange(0, windowWidth - snakeBlock) / 10.0) * 10.0
    appleYPos = round(random.randrange(0, windowHeight - snakeBlock) / 10.0) * 10.0
    lemonXPos = round(random.randrange(0, windowWidth - snakeBlock) / 10.0) * 10.0
    lemonYPos = round(random.randrange(0, windowHeight - snakeBlock - 50) / 10.0) * 10.0
 
    while not gameOver:
 
        while gameClose == True:
            display.fill(grey2)
            message("You Lost! Press R to replay", red)
            playerScore(snakeLength - 1)
            lightX = random.randint(0,7)
            lightY = random.randint(0,7)
            lightR = random.randint(0,255)
            lightG = random.randint(0,255)
            lightB = random.randint(0,255)
            # sense.set_pixel(lightX, lightY, lightR, lightG, lightB)
            pygame.display.update()
        
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameOver = True
                        gameClose = False
                    if event.key == pygame.K_r:
                        # sense.clear(grey)
                        gameLoop()
                        
            while gameOver == True:
                lightX = random.randint(0,7)
                lightY = random.randint(0,7)
                lightR = random.randint(0,255)
                lightG = random.randint(0,255)
                lightB = random.randint(0,255)
                # sense.set_pixel(lightX, lightY, lightR, lightG, lightB)
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    x1_change = -snakeBlock
                    y1_change = 0
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    x1_change = snakeBlock
                    y1_change = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    y1_change = -snakeBlock
                    x1_change = 0
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    y1_change = snakeBlock
                    x1_change = 0
 
        if x1 >= windowWidth or x1 < 0 or y1 >= windowHeight or y1 < 0:
            gameClose = True
        x1 += x1_change
        y1 += y1_change
        display.fill(grey)
        pygame.draw.rect(display, red, [appleXPos, appleYPos, snakeBlock, snakeBlock])
        pygame.draw.rect(display, yellow, [lemonXPos, lemonYPos, snakeBlock, snakeBlock])
        snakeHead = []
        snakeHead.append(x1)
        snakeHead.append(y1)
        snakeList.append(snakeHead)
        if len(snakeList) > snakeLength:
            del snakeList[0]
 
        for x in snakeList[:-1]:
            if x == snakeHead:
                gameClose = True
 
        playerSnake(snakeBlock, snakeList)
        playerScore(snakeLength - 1)
    
         
        pygame.display.update()
 
        if x1 == appleXPos and y1 == appleYPos:
            appleXPos = round(random.randrange(0, windowWidth - snakeBlock) / 10.0) * 10.0
            appleYPos = round(random.randrange(0, windowHeight - snakeBlock - 50) / 10.0) * 10.0
            snakeLength += 1
            # pygame.mixer.music.play(0)
            # sense.clear(red)
            # time.sleep(0.5)
            # sense.clear(grey)
            
        if x1 == lemonXPos and y1 == lemonYPos:
            lemonChance = random.randint(0,2)
            if lemonChance == 0:
                lemonXPos = round(random.randrange(0, windowWidth - snakeBlock) / 10.0) * 10.0
                lemonYPos = round(random.randrange(0, windowHeight - snakeBlock - 50) / 10.0) * 10.0
                snakeLength += 3
                # pygame.mixer.music.play(1)
                # sense.clear(yellow)
                # time.sleep(0.5)
                # sense.clear(grey)        
 
        snakeSpeed = 15
        timer.tick(snakeSpeed)
 
    pygame.quit()
    quit()
  
gameLoop()
