import pygame
import random

pygame.init()

screen_width = 900
screen_height = 600

white = (255,255,255)
black = (0,0,0)
red=(255,0,0)

gameWindow = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Snakes")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None,55)

def score_disp(text, color,x,y):
    screen_text = font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])

def plot_snake(gameWindow,color,snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow,color,[x,y,snake_size,snake_size])    

def game_loop():    
    snk_list=[]
    snk_len = 1
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_init = 5
    velocity_x = 0
    velocity_y = 0
    snake_size = 20
    food_x = random.randint(20,screen_width/1.5)
    food_y = random.randint(20,screen_height/1.5)
    score =0

    while not exit_game:
        if game_over:
            gameWindow.fill(white)
            score_disp("Score: " + str(score),red,350,200)
            score_disp("Game Over! Press Enter to continue! ",red,120,300)

            for event in pygame.event.get():
    
                if event.type == pygame.QUIT:
                    exit_game=True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game_loop()

        else:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    exit_game=True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        if velocity_x == 0:
                            velocity_x = velocity_init
                            velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        if velocity_x == 0:
                            velocity_x = -velocity_init
                            velocity_y = 0
                    if event.key == pygame.K_UP:
                        if velocity_y == 0:
                            velocity_y = -velocity_init
                            velocity_x = 0
                    if event.key == pygame.K_DOWN:
                        if velocity_y == 0:
                            velocity_y = velocity_init
                            velocity_x = 0
                    
            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y
            

            if abs(snake_x-food_x)<15 and abs(snake_y-food_y)<15:
                score = score+10
                food_x = random.randint(20,screen_width/1.5)
                food_y = random.randint(20,screen_height/1.5)
                snk_len+=5

            gameWindow.fill(white)
            score_disp("Score : " + str(score),red,5,5)
            pygame.draw.rect(gameWindow,red,[food_x,food_y,snake_size,snake_size])
            
            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            
            if len(snk_list)>snk_len:
                del snk_list[0]
            
            if head in snk_list[:-1]:
                game_over =True                    

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True

            #pygame.draw.rect(gameWindow,black,[snake_x,snake_y,snake_size,snake_size])
            plot_snake(gameWindow,black,snk_list,snake_size)
        pygame.display.update()
        clock.tick(40)   #fps

    pygame.quit()
    quit()

game_loop()