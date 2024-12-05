import pygame
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball Brain ROT")


BG = (0, 0, 0)
CIRCLE_COLOR = (255, 255, 255)
BALL_COLOR = (200, 50, 50)


crying_emoji = pygame.image.load(r"Project3\crying_emoji.png")
crying_emoji = pygame.transform.scale(crying_emoji, (30, 30))

circle_center = (WIDTH // 2, HEIGHT // 2)
circle_radius = 200


ball_radius = 15
ball_pos = [circle_center[0], circle_center[1]]
ball_velocity = [-8, -6]  
gravity = 0.3

collision_sound = pygame.mixer.Sound(r"Project3\oof.mp3")

clock = pygame.time.Clock()
FPS = 60

running = True
use_emoji = False


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                use_emoji = not use_emoji

    
    ball_velocity[1] += gravity


    ball_pos[0] += ball_velocity[0]
    ball_pos[1] += ball_velocity[1]


    to_ball_x = ball_pos[0] - circle_center[0]
    to_ball_y = ball_pos[1] - circle_center[1]
    distance_to_center = math.sqrt(to_ball_x**2 + to_ball_y**2)


    if distance_to_center + ball_radius > circle_radius:

        collision_sound.play()

        normal_x = to_ball_x / distance_to_center
        normal_y = to_ball_y / distance_to_center
        dot_product = ball_velocity[0] * normal_x + ball_velocity[1] * normal_y
        ball_velocity[0] -= 2 * dot_product * normal_x
        ball_velocity[1] -= 2 * dot_product * normal_y


        overlap = distance_to_center + ball_radius - circle_radius
        ball_pos[0] -= normal_x * overlap
        ball_pos[1] -= normal_y * overlap


    screen.fill(BG)
    pygame.draw.circle(screen, CIRCLE_COLOR, circle_center, circle_radius, 2)
    pygame.draw.circle(screen, BALL_COLOR, (int(ball_pos[0]), int(ball_pos[1])), ball_radius)

    if use_emoji:
        screen.blit(crying_emoji, (int(ball_pos[0]) - 15, int(ball_pos[1]) - 15))
    else:
        pygame.draw.circle(screen, BALL_COLOR, (int(ball_pos[0]), int(ball_pos[1])), ball_radius)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
