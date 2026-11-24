# 1) Import required modules:
#    a) Import `math` to calculate distance for collision detection.
#    b) Import `random` to generate random enemy positions.
#    c) Import `pygame` to create the game window, load images, and handle events.

# 2) Create constants to control game settings:
#    a) Screen size, player start position, enemy start range.
#    b) Enemy movement speed (X and Y), bullet speed, collision distance threshold.

# 3) Initialize pygame using `pygame.init()`.

# 4) Create the game window (screen) using `pygame.display.set_mode(...)`.

# 5) Load background image using `pygame.image.load('background.png')`.

# 6) Set the game title and icon:
#    a) Use `pygame.display.set_caption("Space Invader")`.
#    b) Load icon image `ufo.png` and apply using `pygame.display.set_icon(icon)`.

# 7) Setup the player:
#    a) Load the player image `player.png`.
#    b) Set initial player position using `playerX` and `playerY`.
#    c) Create `playerX_change = 0` to control horizontal movement.

# 8) Setup enemies using lists (multiple enemies):
#    a) Create empty lists for enemy image, x/y positions, and x/y movement changes.
#    b) Set `num_of_enemies = 6`.

# 9) Use a loop to create each enemy:
#    a) Load enemy image `enemy.png` and append it to `enemyImg`.
#    b) Set random starting X position within the screen width.
#    c) Set random starting Y position between ENEMY_START_Y_MIN and ENEMY_START_Y_MAX.
#    d) Set initial X speed (ENEMY_SPEED_X) and Y drop speed (ENEMY_SPEED_Y).

# 10) Setup bullet:
#     a) Load bullet image `bullet.png`.
#     b) Set bullet starting positions and movement speed.
#     c) Use `bullet_state = "ready"` to track if bullet can be fired or is already moving.

# 11) Setup score display:
#     a) Initialize `score_value = 0`.
#     b) Load a font using `pygame.font.Font(...)`.
#     c) Set score text position (textX, textY).

# 12) Setup game-over text font using a larger font size.

# 13) Define helper functions:
#     a) `` to render and display the score on the screen.
#     b) `game_over_text()` to display "GAME OVER" on the screen.
#     c) `player(x, y)` to draw the player image at (x, y).
#     d) `enemy(x, y, i)` to draw the i-th enemy at (x, y).
#     e) `fire_bullet(x, y)`:
#        - Set `bullet_state` to "fire"
#        - Draw the bullet slightly offset from the player position.
#     f) `isCollision(enemyX, enemyY, bulletX, bulletY)`:
#        - Calculate distance between enemy and bullet using the distance formula.
#        - Return True if distance is less than COLLISION_DISTANCE.

# 14) Start the main game loop with ``.

# 15) Every frame inside the loop:
#     a) Clear the screen and draw the background image.

# 16) Handle events (keyboard and quit):
#     a) If `pygame.QUIT`, stop the loop.
#     b) If a key is pressed (`pygame.KEYDOWN`):
#        - LEFT arrow sets `playerX_change = -5`.
#        - RIGHT arrow sets `playerX_change = 5`.
#        - SPACE fires the bullet only if `bullet_state` is "ready":
#          i) Set `bulletX = playerX`
#          ii) Call `fire_bullet(bulletX, bulletY)`
#     c) If key is released (`pygame.KEYUP`) for LEFT/RIGHT:
#        - Set `playerX_change = 0` to stop movement.

# 17) Update player movement:
#     a) Add `playerX_change` to `playerX`.
#     b) Clamp player position so it stays inside the screen boundaries.

# 18) Update enemy movement for each enemy:
#     a) If any enemy goes below Y > 340:
#        - Move all enemies off-screen (enemyY = 2000)
#        - Display "GAME OVER"
#        - Break out of enemy loop.
#     b) Move enemy horizontally using `enemyX_change[i]`.
#     c) If enemy hits left/right edge:
#        - Reverse direction by multiplying speed by -1.
#        - Move enemy downward by adding `enemyY_change[i]`.
#     d) Check collision between the enemy and bullet:
#        - If collision occurs:
#          i) Reset bullet position and set bullet_state back to "ready".
#          ii) Increase score by 1.
#          iii) Respawn enemy at a new random position.
#     e) Draw the enemy on the screen.

# 19) Update bullet movement:
#     a) If bullet goes off the top of the screen (`bulletY <= 0`):
#        - Reset bulletY and set `bullet_state = "ready"`.
#     b) If bullet_state is "fire":
#        - Draw the bullet.
#        - Move the bullet upward by decreasing `bulletY`.

# 20) Draw the player, show the score, and update the display:
#     a) Draw player at (playerX, playerY).
#     b) Display score using `show_score(textX, textY)`.
#     c) Refresh the screen using `pygame.display.update()`.

print("Space Invaders by : Tomohiro Nishikado")
import math
import random
import pygame
screen_width=800
screen_height=500
player_start_x=370
player_start_y=380
enemy_start_ymin=50
enemy_start_ymax=50
enemy_speed_x=0.25
enemy_speed_y=0.25
bullet_speed_y=10
collision_dist=27
pygame.init()
screen=pygame.display.set_mode((screen_width,screen_height))
bgimg=pygame.transform.scale(pygame.image.load('bggrnd.jpg').convert(),(screen_width,screen_height))
caption=pygame.display.set_caption("Space Invader")
icon=pygame.image.load('rcket.png')
pygame.display.set_icon(icon)
playerimg=pygame.image.load('rcket.png')
playerx=player_start_x
playery=player_start_y
playerx_change=0
enemyimg=[pygame.image.load('enem1.png'),pygame.image.load('enem2.png'),pygame.image.load('enem1.png'),pygame.image.load('enem2.png'),pygame.image.load('enem1.png'),pygame.image.load('enem2.png')]
enemyx=[]
enemyy=[]
enemyy_change=[]
enemyx_change=[]
for i in range(6):
    enemyx.append(random.randint(0,screen_width-64))
    enemyy.append(random.randint(enemy_start_ymin,enemy_start_ymax))
    enemyx_change.append(enemy_speed_x)
    enemyy_change.append(enemy_speed_y)
bulletimg=pygame.image.load('bllt.png')
bulletx=0
bullety=player_start_y
bulletx_change=0
bullety_change=bullet_speed_y
bullet_state='ready'
score_value = 0
font=pygame.font.Font("freesansbold.ttf", 32)
textx=10
texty=10
game_over_font=pygame.font.Font("freesansbold.ttf", 48)
def show_score(x, y):
    score=font.render('SCORE : '+str(score_value),True,pygame.Color('white'))
    screen.blit(score,(x,y))
def Game_over_text():
    u_lose=game_over_font.render('GAME OVER (u noob)'+str(),True,pygame.Color('white'))
    screen.blit(u_lose,(200,250))
def player_img(x,y):
    screen.blit(playerimg,(x,y))
def enemy(x,y,i):
    screen.blit(enemyimg[i],(x,y))
def fire_bullet(x,y):
    global bullet_state
    bullet_state='fire'
    screen.blit(bulletimg,(x+16,y+10))
def isCollision(enemyx,enemyy,bulletx,bullety):
    distance=math.sqrt((enemyx-bulletx)**2+(enemyy-bullety)**2)
    return distance < collision_dist
running = True
while running:
    screen.fill(pygame.Color('black'))
    screen.blit(bgimg,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerx_change=-1
            if event.key == pygame.K_RIGHT:
                playerx_change=1
            if event.key == pygame.K_SPACE and bullet_state == 'ready':
                bulletx=playerx
                fire_bullet(bulletx,bullety)
        if event.type == pygame.KEYUP and event.key in [pygame.K_LEFT,pygame.K_RIGHT]:
            playerx_change=0
    playerx+=playerx_change
    playerx=max(0,min(playerx,screen_width-64))
    for i in range(6):
        if enemyy[i]>340:
            for j in range(6):
                enemyy[j]=2000
            Game_over_text()
            break
        enemyx[i]+=enemyx_change[i]
        if enemyx[i]<=0 or enemyx[i]>=screen_width-64:
            enemyx_change[i]*=-1
            enemyy[i]+=enemyy_change[i]
        if isCollision(enemyx[i],enemyy[i],bulletx,bullety):
            bullety=player_start_y
            bullet_state='ready'
            score_value+=1
            enemyx[i]=random.randint(0,screen_width-64)
            enemyy[i]=random.randint(enemy_start_ymin,enemy_start_ymax)
        enemy(enemyx[i],enemyy[i],i)
    if bullety<=0:
        bullety=player_start_y
        bullet_state='ready'
    elif bullet_state == 'fire':
        fire_bullet(bulletx,bullety)
        bullety-=bullety_change
    player_img(playerx,playery)
    show_score(textx,texty)
    pygame.display.flip()
pygame.quit()