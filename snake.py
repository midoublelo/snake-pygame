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

pygame.mixer.init
appleSound = pygame.mixer.music.load("apple.ogg")
lemonSound = pygame.mixer.music.load("lemon.ogg")
 
display = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("Snake in Pygame")
 
timer = pygame.time.Clock()
 
snakeBlock = 10
snakeSpeed = 10
 
font_style = pygame.font.SysFont("linuxlibertineo", 25)
score_font = pygame.font.SysFont("linuxlibertineo", 35)

# sense.clear(grey)

def playerScore(score):
    value = score_font.render("Your Score: " + str(score), True, black)
    display.blit(value, [0, 0])
 
def playerSnake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, green, [x[0], x[1], snakeBlock, snakeBlock])
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [windowWidth / 6, windowHeight / 3])
 
def gameLoop():
    game_over = False
    game_close = False
 
    x1 = windowWidth / 2
    y1 = windowHeight / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1
 
    foodXPos = round(random.randrange(0, windowWidth - snakeBlock) / 10.0) * 10.0
    foodYPos = round(random.randrange(0, windowHeight - snakeBlock) / 10.0) * 10.0
    powerUpXPos = round(random.randrange(0, windowWidth - snakeBlock) / 10.0) * 10.0
    powerUpYPos = round(random.randrange(0, windowHeight - snakeBlock - 50) / 10.0) * 10.0
 
    while not game_over:
 
        while game_close == True:
            display.fill(grey2)
            message("You Lost! Press R to replay", red)
            playerScore(Length_of_snake - 1)
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
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        # sense.clear(grey)
                        gameLoop()
                        
            while game_over == True:
                lightX = random.randint(0,7)
                lightY = random.randint(0,7)
                lightR = random.randint(0,255)
                lightG = random.randint(0,255)
                lightB = random.randint(0,255)
                # sense.set_pixel(lightX, lightY, lightR, lightG, lightB)
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
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
            game_close = True
        x1 += x1_change
        y1 += y1_change
        display.fill(grey)
        pygame.draw.rect(display, red, [foodXPos, foodYPos, snakeBlock, snakeBlock])
        pygame.draw.rect(display, yellow, [powerUpXPos, powerUpYPos, snakeBlock, snakeBlock])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        playerSnake(snakeBlock, snake_List)
        playerScore(Length_of_snake - 1)
    
         
        pygame.display.update()
 
        if x1 == foodXPos and y1 == foodYPos:
            foodXPos = round(random.randrange(0, windowWidth - snakeBlock) / 10.0) * 10.0
            foodYPos = round(random.randrange(0, windowHeight - snakeBlock - 50) / 10.0) * 10.0
            Length_of_snake += 1
            pygame.mixer.music.play(0)
            # sense.clear(red)
            # time.sleep(0.5)
            # sense.clear(grey)
            
        if x1 == powerUpXPos and y1 == powerUpYPos:
            powerUpChance = random.randint(0,2)
            if powerUpChance == 0:
                powerUpXPos = round(random.randrange(0, windowWidth - snakeBlock) / 10.0) * 10.0
                powerUpYPos = round(random.randrange(0, windowHeight - snakeBlock - 50) / 10.0) * 10.0
                Length_of_snake += 3
                pygame.mixer.music.play(1)
                # sense.clear(yellow)
                # time.sleep(0.5)
                # sense.clear(grey)        
 
        snakeSpeed = 15
        timer.tick(snakeSpeed)
 
    pygame.quit()
    quit()
  
gameLoop()