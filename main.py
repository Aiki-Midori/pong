# IM PROUD OF THIS!!!
import pygame as pg, sys, random

pg.init()

w, h = 1200, 600
white = "#ffffff"
screen = pg.display.set_mode((w, h))
clock = pg.time.Clock()
font = pg.font.Font('font/Pixeltype.ttf', 50)
FPS = 50
p1_score = 0
p2_score = 0
player_length = 50

p_speed = 5
player_surf = pg.Surface((10, h/6))
player_surf.fill(white)
player1_rect = player_surf.get_rect(center=(player_length, h/2))
player2_rect = player_surf.get_rect(center=(w-player_length, h/2))

ball_speed = 4
ball_velx = random.choice([ball_speed, -ball_speed])
ball_vely = random.choice([ball_speed, -ball_speed])
ball_surf = pg.Surface((15, 15))
ball_surf.fill(white)
ball_rect = ball_surf.get_rect(center=(w/2, h/2))

def reset_ball():
    ball_rect.center = (w/2, h/2)
    global ball_velx, ball_vely
    ball_velx = random.choice([ball_speed, -ball_speed])
    ball_vely = random.choice([ball_speed, -ball_speed])
    
while True:
    screen.fill((20, 30, 20))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    screen.blit(player_surf, player1_rect)
    screen.blit(player_surf, player2_rect)
    screen.blit(ball_surf, ball_rect)

    p1_text_surf = font.render(f"{p1_score}", False, (white))
    p2_text_surf = font.render(f"{p2_score}", False, (white))
    screen.blit(p1_text_surf, (w/4, 50))
    screen.blit(p2_text_surf, (w-w/4, 50))

    keys = pg.key.get_pressed()
    if keys[pg.K_UP]: 
        player2_rect.centery -= p_speed
        if player2_rect.centery <= player_length: player2_rect.centery = player_length
    if keys[pg.K_DOWN]: 
        player2_rect.centery += p_speed
        if player2_rect.centery >= h-player_length: player2_rect.centery = h-player_length
    if keys[pg.K_w]: 
        player1_rect.centery -= p_speed
        if player1_rect.centery <= player_length: player1_rect.centery = player_length
    if keys[pg.K_s]: 
        player1_rect.centery += p_speed
        if player1_rect.centery >= h-player_length: player1_rect.centery = h-player_length


    ball_rect.centerx += ball_velx
    ball_rect.centery += ball_vely
    if ball_rect.centery < 15:  ball_vely *= -1
    if ball_rect.centery > h-15: ball_vely *= -1
    if ball_rect.centerx < 15: 
        p2_score += 1
        reset_ball()
    if ball_rect.centerx > w-15: 
        p1_score += 1
        reset_ball()

    if player1_rect.colliderect(ball_rect) or player2_rect.colliderect(ball_rect): 
        ball_velx *= -1
        if ball_velx > 0: ball_velx += 0.5
        elif ball_velx < 0: ball_velx -= 0.5

    pg.display.update()
    clock.tick(FPS)





# --------- TODO --------- #
    # draw players onto the screen
    # control players
    # add ball on the middle
    # make ball move on zigzag either left/right, up/down
    # add boundaries
    # make ball bounce on, boundaries;continuing x dir but opp y dir
    # detect collision on players; opp x dir
    # add score system
    # make ball faster every collision
    # done!!
