import pygame
import sys 

from pygame import Vector2
import random 

def new_game() : 
    pygame.mixer.init()

    pygame.init()
    cell_size =30
    cell_number =20
    screen = pygame.display.set_mode((cell_number*cell_size,cell_number*cell_size))
    clock = pygame.time.Clock()

    class FRUIT :
        def __init__(self):
            self.randomize()
        def  draw_fruit(self):
            fruit_rect = pygame.Rect(int(self.pos.x *cell_size) ,int( self.pos.y* cell_size ), cell_size , cell_size)
            screen.blit(appele ,fruit_rect)
        def randomize (self):
            self.pos = Vector2(random.randint(0, cell_number - 1), random.randint(0, cell_number - 1))


    class SNAKE :
        def __init__(self):
            self.body = [Vector2(5 , 10), Vector2 (4,10) , Vector2(3 ,10)]
            self.direction =Vector2(0,0)
            self.new_block = False

            self.head_right = pygame.image.load('head_right.png').convert_alpha()
            self.head_left = pygame.image.load('head_left.png').convert_alpha()
            self.head_up = pygame.image.load('head_up.png').convert_alpha()
            self.head_down = pygame.image.load('head_down.png').convert_alpha()
            
            self.tail_right = pygame.image.load('end_right.png').convert_alpha()
            self.tail_left = pygame.image.load('end_left.png').convert_alpha()
            self.tail_up = pygame.image.load('end_up.png').convert_alpha()
            self.tail_down = pygame.image.load('end_down.png').convert_alpha()


            self.body_vertical = pygame.image.load('body_vertical.png').convert_alpha()
            self.body_horintal = pygame.image.load('body_horizontal.png').convert_alpha()


            self.body_tr = pygame.image.load('body_tr.png').convert_alpha()
            self.body_tl = pygame.image.load('body_tl.png').convert_alpha()
            self.body_br = pygame.image.load('body_br.png').convert_alpha()
            self.body_bl = pygame.image.load('body_bl.png').convert_alpha()

            self.crunch_sound = pygame.mixer.Sound('feed.wav')
            self.crunch_sound_fail = pygame.mixer.Sound('fail.wav')
            self.crunch_sound_move = pygame.mixer.Sound('move2.wav')
            
        def draw_snake(self):
            self.update_head_graphics()
            self.update_tail_graphics()
            for index , block in enumerate(self.body):
                x_pos = int(block.x*cell_size)
                y_pos = int(block.y*cell_size)
                block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)

                
                if index == 0:
                    screen.blit(self.head, block_rect)
                elif index == len(self.body) - 1:
                    screen.blit(self.tail,block_rect)
                

                else :
                    previous_block = self.body[index +1 ] - block 
                    next_block = self.body[index -1] - block
                    if previous_block.x == next_block.x:
                        screen.blit(self.body_horintal , block_rect)
                    elif previous_block.y == next_block.y:
                        screen.blit(self. body_vertical , block_rect)
                    else :
                        if previous_block.x == -1 and next_block.y==-1 or previous_block.y == -1 and next_block.x == -1 :
                            screen.blit(self.body_tl , block_rect)
                        elif previous_block.x == -1 and next_block.y==1 or previous_block.y == 1 and next_block.x == -1 :
                            screen.blit(self.body_bl , block_rect)
                        elif previous_block.x == 1 and next_block.y==-1 or previous_block.y == -1 and next_block.x == 1 :
                            screen.blit(self.body_tr , block_rect)
                        elif previous_block.x == 1 and next_block.y==1 or previous_block.y == 1 and next_block.x == 1 :
                            screen.blit(self.body_br , block_rect)




                
                    #pygame.draw.rect(screen, (150, 100, 100), block_rect)

        def update_tail_graphics(self):
                tail_relation = self.body[-1] - self.body[-2]
                if tail_relation == Vector2(1, 0): self.tail = self.tail_left
                elif tail_relation == Vector2(-1, 0): self.tail = self.tail_right
                elif tail_relation == Vector2(0, -1): self.tail = self.tail_down
                elif tail_relation == Vector2(0, 1): self.tail = self.tail_up

        def update_head_graphics(self):
            head_relation = self.body[1] - self.body[0]
            if head_relation == Vector2(1,0): self.head = self.head_left
            elif head_relation == Vector2(-1,0): self.head = self.head_right
            elif head_relation == Vector2(0,-1): self.head = self.head_down
            elif head_relation == Vector2(0,1): self.head = self.head_up


                

            # for block in self.body :
            #     x_pos = int(block.x*cell_size)
            #     y_pos = int(block.y*cell_size)
            #     block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)
            #     pygame.draw.rect(screen,(221,83,128),block_rect)
        
        def move_snake(self):
            if self.new_block:
                body_copy = self.body[:]
                if self.direction != Vector2(0,0):
                    self.crunch_sound_move.set_volume(0.1)
                    self.crunch_sound_move.play()
                else:
                    self.crunch_sound_move.stop()

            else:
                body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
            if self.direction != Vector2(0,0):
                self.crunch_sound_move.set_volume(0.1)
                self.crunch_sound_move.play()
            else:
                    self.crunch_sound_move.stop()

        def add_block (self):
            self.new_block = True

        def play_crunch_sound (self):
            self.crunch_sound.play()
        def play_dound_move(self):
            self.crunch_sound_move.play()
        def reset(self):
            self.body = [Vector2(5 , 10), Vector2 (4,10) , Vector2(3 ,10)]
            self.direction =Vector2(0,0)
            
    class MAIN :
        def __init__(self):
            self.snake = SNAKE()
            self.fruit = FRUIT()
            
        def update(self):
            self.snake.move_snake()
            self.snake.play_dound_move()
            self.check_collision()
            self.check_fail()
            if self.fruit.pos == self.snake.body[0]:
                self.fruit.randomize()

        def draw_elements (self):
            self.draw_gress()
            self.snake.draw_snake()
            self.fruit.draw_fruit()
            self.draw_score()


        def check_collision(self):
            if self.fruit.pos == self.snake.body[0]:
                self.fruit.randomize()
                self.snake.add_block()
                self.snake.crunch_sound_move.stop()
                self.snake.crunch_sound.set_volume(0.6)
                self.snake.crunch_sound.play()
                self.snake.crunch_sound_move.play()
            for block in self.snake.body[1:] :
                if block == self.fruit.pos :
                    self.fruit.randomize()
    
        def check_fail (self):
            if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number :
                self.gameOver()
            for block in self.snake.body[1:]:
                if block ==self.snake.body[0]:
                    self.gameOver()

        def gameOver(self):
            self.snake.crunch_sound_move.stop()
            if self.snake.direction != Vector2(0,0):
                self.snake.crunch_sound_fail.play()
            self.snake.reset()
        
        def draw_gress(self):
            grass_color = (150, 200, 100)
            for row in range(cell_number):
                if row % 2 == 0 :
                    for col in range(cell_number):
                        if col % 2 == 0:
                            grass_rect = pygame.Rect(col * cell_size ,row *cell_size,cell_size ,cell_size)
                            pygame.draw.rect(screen,grass_color ,grass_rect)
                else:
                    for col in range(cell_number):
                        if col % 2 != 0:
                            grass_rect = pygame.Rect(col * cell_size ,row *cell_size,cell_size ,cell_size)
                            pygame.draw.rect(screen,grass_color ,grass_rect)
        
        def draw_score(self):
            score_text = str(len(self.snake.body) - 3)
            game_font = pygame.font.Font(None, 26)
            score_surface = game_font.render(score_text, True, (0, 0, 0))
            score_x = int(cell_size * cell_number - 60)
            score_y = int(cell_size * cell_number - 40)
            score_rect = score_surface.get_rect(center=(score_x, score_y))
            appele_rect = appele.get_rect(midright = (score_rect.left -2, score_rect.centery))
            bg_rect = pygame.Rect(appele_rect.left ,appele_rect.top ,appele_rect.width  + score_rect.width +5,appele_rect.height )

            pygame.draw.rect(screen , ('white') ,bg_rect)
            screen.blit(score_surface, score_rect)
            screen.blit(appele1,appele_rect)
            pygame.draw.rect(screen,(0,0,0),bg_rect,2)
        


    pygame.mixer.pre_init(4410,-16 ,2,512)
    appele = pygame.image.load('appele.png').convert_alpha()
    appele1 = pygame.image.load('image_for.png').convert_alpha()

    game_font = pygame.font.Font('Score_is_better.ttf' , 25)
    main_game = MAIN()
    SCREEN_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE ,150)




    while True :
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                pygame.quit()
                sys.exit()

        
            if event.type == SCREEN_UPDATE:
                main_game.update()

            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_UP :
                    if main_game.snake.direction.y != 1 :
                        main_game.snake.direction = Vector2(0,-1)



                if event.key == pygame.K_LEFT :
                    if main_game.snake.direction.x != 1 :
                        main_game.snake.direction = Vector2(-1,0)
                


                
                if event.key == pygame.K_DOWN :
                    if main_game.snake.direction.y != -1 :
                        main_game.snake.direction = Vector2(0,1)

                if event.key == pygame.K_RIGHT :
                    if main_game.snake.direction.x != -1 :
                        main_game.snake.direction = Vector2(1,0)

            
        
        screen.fill(pygame.Color('white'))
        #screen.blit(test_surface , (200, 250))
        main_game.draw_elements()
        main_game.check_collision()
        main_game.check_fail()




        pygame.display.update()
        clock.tick(20)
