# pygame template

import pygame


pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables
grass = [(0,330), (0,HEIGHT), ( 640, HEIGHT), (640, 330)]
tower_roof = [(400,25) , (350,150), (450 ,150)]
tower = [(365,150), (435,150), (440,350),(360,350)]
house_left = [(280,350),(360 ,350), (370 , 220),( 280 , 220)]
house_left_roof = [(270 , 220) , (300 ,170) , (365 ,170),(365,220)]
house_right = [(435,350) , (435 , 270) , (470 , 270), (470 , 350)]
house_right_roof = [(435 , 270), (430 , 240) , (480, 270)]
wp1 = 380
wp2 =180
window_width = 40
window_pt1 =[(wp1,wp2), (wp1+window_width ,wp2), (wp1+window_width ,wp2+55), (wp1,wp2+55)]
window_pt2 =[(wp1 +window_width/2), (wp2)]
window_offset_wp1= -85
window_offset_wp2 = 80
window_pt12 =[(wp1 + window_offset_wp1 ,wp2 + window_offset_wp2), (wp1+window_width +window_offset_wp1 ,wp2 +window_offset_wp2), (wp1+window_width+window_offset_wp1 ,wp2+55+ window_offset_wp2), (wp1 +window_offset_wp1,wp2+55 + window_offset_wp2)]
window_pt22 =[(wp1 +window_width/2 +window_offset_wp1), (wp2 + window_offset_wp2)]
window_colour = [(70), (151), (225) ]
center_window_1 = [(400,235) ,(400,235), (400 ,160),(400 ,160)]
center_window_2 = [(400+window_offset_wp1,235+window_offset_wp2) ,(400+window_offset_wp1,235+window_offset_wp2), (400+window_offset_wp1 ,160+window_offset_wp2),(400+window_offset_wp1 ,160+window_offset_wp2)]
door = [(380,280), (380,350) , (415,350) , (415,280)]
shift_x = 100
shift_y = 100
shift_x_v = 5
shift_y_v = 5
size = 0.5
border = int(5 * size)
time = 1
time_s = 0
condtion =0
background =(135, 206, 235)
grass_colour = (124, 252, 0)
# ---------------------------

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
    
    time_s += 1
    if time_s == 300:
        time = -time
        time_s = 0
        condtion =1
    if time == -1:
        background = (135, 206, 235)
        grass_colour = (124, 252, 0)
        shift_x = 250
        shift_y = 320
        shift_x_v = 0
        shift_y_v = 0
        size=0.25
    elif time == 1 and condtion ==1:
        background = (27, 41, 47)
        grass_colour = (25, 50, 0)
        shift_x_v =5
        shift_y_v = 5
        size = 0.5
        condtion =0


    # GAME STATE UPDATES
    shift_x += shift_x_v
    shift_y += shift_y_v
    shift_y_v +=0.1

    # All game math and comparisons happen here
    f_a_c = (shift_x ,shift_y ,size * 100 , size * 150)
    left = (shift_x - size * 25, shift_y - size * 10, size * 100 ,size * 150)
    right = (shift_x + size * 25, shift_y - size * 10 , size * 100 ,size * 150)
    stem = [(shift_x+ size * 50 , shift_y - size * 20), (shift_x+ size * 55 , shift_y- size * 20) , (shift_x+ size * 60,shift_y+ size * 10) , (shift_x+ size * 40, shift_y+ size * 10)]
    eye_1 = [(shift_x + size *30 , shift_y+size *40) , (shift_x +size *20 , shift_y+size *60) , (shift_x+size *40 , shift_y +size *60)]
    eye_2 = [(shift_x + size *70 , shift_y+size *40) , (shift_x +size *60 , shift_y+size *60) , (shift_x+size *80 , shift_y +size *60)]
    mouth = [(shift_x +size *20 , shift_y +size *100) , (shift_x +size *30 ,shift_y +size *120) , (shift_x +size *40 ,shift_y +size *110)  , (shift_x +size *60 ,shift_y +size *115)  , (shift_x +size *70 ,shift_y +size *100) , (shift_x +size *60 ,shift_y +size *90) , (shift_x +size *45 ,shift_y +size *100)]


   
    if shift_x >= WIDTH -125 * size or shift_x < 25 * size:
        shift_x_v = -shift_x_v
   
    if shift_y >= HEIGHT - 150 *size   or shift_y < 20 *size:
        shift_y_v = -shift_y_v
    # DRAWING
    screen.fill((background))  # always the first drawing command

    

    pygame.draw.polygon(screen , (grass_colour), (grass))
    pygame.draw.polygon(screen , (128, 76, 31), (house_left))
    pygame.draw.polygon(screen , (0, 0, 0), (house_left) ,5)
    pygame.draw.polygon(screen , (61, 49, 39), (house_left_roof))
    pygame.draw.polygon(screen , (0, 0, 0), (house_left_roof) ,5)
    pygame.draw.polygon(screen , (128, 76, 31), (house_right))
    pygame.draw.polygon(screen , (0, 0, 0), (house_right) ,5)
    pygame.draw.polygon(screen , (61,49,39), (house_right_roof))
    pygame.draw.polygon(screen , (0 , 0 ,0), (house_right_roof) , 5)    
    pygame.draw.polygon(screen , (61, 49, 39), (tower_roof))
    pygame.draw.polygon(screen , (0, 0, 0), (tower_roof) ,5)
    pygame.draw.polygon(screen , (128, 76, 31), (tower))
    pygame.draw.polygon(screen , (0, 0, 0), (tower) ,5)
    pygame.draw.circle(screen, (window_colour), (window_pt2), window_width/2)
    pygame.draw.circle(screen, (0,0,0), (window_pt2), window_width/2, 3)
    pygame.draw.polygon(screen, (window_colour), (window_pt1))
    pygame.draw.polygon(screen, (0,0,0), (window_pt1),3)
    pygame.draw.circle(screen, (window_colour), (window_pt22), window_width/2)
    pygame.draw.circle(screen, (0,0,0), (window_pt22), window_width/2,3)
    pygame.draw.polygon(screen, (window_colour), (window_pt12))
    pygame.draw.polygon(screen, (0,0,0), (window_pt12),3)
    pygame.draw.polygon(screen, (0,0,0) , (center_window_1),3)
    pygame.draw.polygon(screen, (0,0,0) , (center_window_2),3)
    pygame.draw.polygon(screen, (128,0,32), (door))
    pygame.draw.polygon(screen, (0,0,0), (door),3)
    pygame.draw.ellipse(screen, ( 255, 117, 24) , (left) )
    pygame.draw.ellipse(screen, ( 0,0,0) , (left) , border)
    pygame.draw.ellipse(screen, ( 255, 117, 24) , (right) )
    pygame.draw.ellipse(screen, ( 0,0,0) , (right) , border)
    pygame.draw.polygon(screen, (138, 171, 70) , (stem))
    pygame.draw.polygon(screen, (0,0,0), (stem) , border)
    pygame.draw.ellipse(screen, ( 255, 117, 24) , (f_a_c) )
    pygame.draw.ellipse(screen, ( 0,0,0) , (f_a_c) , border)
    pygame.draw.polygon(screen, (0,0,0), (eye_1))
    pygame.draw.polygon(screen, (0,0,0), (eye_2))
    pygame.draw.polygon(screen, (0,0,0), (mouth))
    if time == -1:
        pygame.draw.circle(screen, (225,225,225), (100,100), 25)
    if time == 1:
        pygame.draw.circle(screen, (225,225,225), (100,100), 25)
        pygame.draw.circle(screen, (27, 41, 47), (105,95), 25)
    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit()