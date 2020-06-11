import pygame
import random
pygame.init()
pygame.mixer.init()
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
screen_width=1000
screen_height=500
bimg=pygame.image.load("WelcomeImage.jpg")
bimg=pygame.transform.scale(bimg, [screen_width, screen_height])
gimg=pygame.image.load("Background.jpg")
gimg=pygame.transform.scale(gimg, [screen_width, screen_height])
clock=pygame.time.Clock()
gamewindow=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Snake Game (By Shoham)")
pygame.display.update()
font=pygame.font.SysFont('Arial', 40, False,True)
def text_Hover(text,color,x,y):
    screen_text=font.render(text, True, color)
    gamewindow.blit(screen_text,[x,y])
def snake_shape(screen,color,head,snake_size):
    for x,y in head:
        pygame.draw.rect(screen,color, [x,y,snake_size,snake_size])
def WELCOME():
    exit_game=False
    while not exit_game:
        gamewindow.fill(white)
        gamewindow.blit(bimg,[0,0])
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game=True
            if event.type == pygame.KEYDOWN:
                pygame.mixer.music.load("Divine_Life_Society.mp3")
                pygame.mixer.music.play()
                game_loop()
                

    pygame.quit()
    quit()
def game_loop():
    exit_game=False
    game_over=False
    snake_x=40
    snake_y=60
    velocity_value=2
    snake_size=30
    snake_list=[]
    snake_length=1
    food_x=random.randint(50,screen_width-50)
    food_y=random.randint(50,screen_height-50)
    fps=60
    velocity_x=0
    velocity_y=0
    score=0
    with open("HS.txt") as f:
        highscore=f.read()
    while not exit_game:
        if game_over:
            gamewindow.fill(white)
            gamewindow.blit(gimg,[0,0])
            pygame.display.update()
            pygame.mixer.music.load("Divine_Life_Society.mp3")
            pygame.mixer.music.pause() 
            with open("HS.txt","wt") as f:
                f.write(str(highscore))
            text_Hover("Game Over Press Enter any key to Continue",red,200,200)
            text_Hover("Your Score is:"+str(score),red,380,250)
            text_Hover("HighScore was:"+str(highscore),red,380,300)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game=True
                if event.type == pygame.KEYDOWN:
                    pygame.mixer.music.load("Divine_Life_Society.mp3")
                    pygame.mixer.music.play()
                    game_loop()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game=True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x=velocity_value
                        velocity_y=0
                    if event.key == pygame.K_LEFT:
                        velocity_x=-velocity_value
                        velocity_y=0
                    if event.key == pygame.K_DOWN:
                        velocity_y=velocity_value
                        velocity_x=0
                    if event.key == pygame.K_UP:
                        velocity_y=-velocity_value
                        velocity_x=0
            snake_x+=velocity_x
            snake_y+=velocity_y
            if abs(food_x-snake_x)<25 and abs(food_y-snake_y)<26:
                food_x=random.randint(20,screen_width-20)
                food_y=random.randint(20,screen_height-20)
                score+=10
                exit_score=score
                snake_length+=5
                velocity_value+=1
            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over=True
            gamewindow.fill(black)
            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)
            if len(snake_list) > snake_length:
                del snake_list[0]
            if head in snake_list[:-1]:
                game_over=True
            if score>int(highscore):
                highscore=score
            text_Hover("Score:"+str(score),red,10,5)
            pygame.draw.rect(gamewindow, red, [food_x,food_y,snake_size,snake_size])
            snake_shape(gamewindow,white,snake_list,snake_size)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()
WELCOME()
game_loop()