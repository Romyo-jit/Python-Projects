import pygame
import sys

# 1. Initialize all imported pygame modules
pygame.init()

# 2. Set up the game display window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption("My First Pygame Example")

# 3. Define basic RGB color constants
WHITE = (255, 255, 255)
BLUE = (0, 100, 255)

# 4. Set up the player object (X, Y, width, height)
player_rect = pygame.Rect(375, 275, 50, 50)
player_speed = 5

# 5. Initialize the game loop clock
clock = pygame.time.Clock()
is_running = True

addx = True
addy = True
# --- MAIN GAME LOOP ---
while is_running:

    # 6. Event Handling Loop (Checks inputs and window interactions)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    # 7. Real-time Keyboard State Input Processing
    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_LEFT] or keys[pygame.K_a]:
    #     player_rect.x -= player_speed
    # if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
    #     player_rect.x += player_speed
    # if keys[pygame.K_UP] or keys[pygame.K_w]:
    #     player_rect.y -= player_speed
    # if keys[pygame.K_DOWN] or keys[pygame.K_s]:
    #     player_rect.y += player_speed
    if (player_rect.x + player_speed > SCREEN_WIDTH - 50) or not addx:
        if (player_rect.x - player_speed < 0):
            addx = True
            player_rect.x += player_speed
        else:
            addx = False
            player_rect.x -= player_speed
    else:
        addx = True
        player_rect.x += player_speed
        
        
    if (player_rect.y + player_speed > SCREEN_HEIGHT - 50) or not addy:
        if (player_rect.y - player_speed < 0):
            addy = True
            player_rect.y += player_speed
        else:
            addy = False
            player_rect.y -= player_speed
    else:
        addy = True
        player_rect.y += player_speed

    # 8. Render Section (Drawing elements on the screen)
    screen.fill(WHITE) # Always clear the screen first
    pygame.draw.rect(screen, BLUE, player_rect) # Draw the player

    # 9. Flip/Update the display buffer to make visuals visible
    pygame.display.flip()

    # 10. Frame Rate Regulation (Locks game logic to 60 Frames Per Second)
    clock.tick(60)

# --- CLEAN UP AND EXIT ---
pygame.quit()
sys.exit()