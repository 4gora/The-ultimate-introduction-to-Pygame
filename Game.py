import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
test_font = pygame.font.Font("font/Pixeltype.ttf", 50)

sky_surf = pygame.image.load("graphics/Sky.png").convert()
ground_surf = pygame.image.load("graphics/ground.png").convert()

score_surf = test_font.render("Meu jogo", False, "black").convert()
score_rect = score_surf.get_rect(center=(screen.get_width() // 2, 100))

snail_surf = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_rect = snail_surf.get_rect(midbottom=(800, 300))

player_surf = pygame.image.load("graphics/player/player_walk_1.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80, 300))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        """ if event.type == pygame.MOUSEMOTION:
            if player_rect.collidepoint(event.pos):
                print("Collide player") """

    screen.blit(sky_surf, (0, 0))
    screen.blit(ground_surf, (0, 300))
    screen.blit(score_surf, score_rect)
    screen.blit(snail_surf, snail_rect)
    screen.blit(player_surf, player_rect)

    snail_rect.x -= 4
    if snail_rect.right < -0:
        snail_rect.left = 800

    pygame.display.update()
    clock.tick(60)

# Drawing with rectangles 1:17:44