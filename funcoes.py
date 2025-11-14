import sys
import pygame

#Move a nave para a direita e esquerda
def check_keydown_events(event, nave_j):
    """Responde a teclas pressionadas"""
    if event.key == pygame.K_RIGHT:
        nave_j.movimento_right = True
    elif event.key == pygame.K_LEFT:
        nave_j.movimento_left = True
    elif event.key == pygame.K_UP:
        nave_j.movimento_up = True
    elif event.key == pygame.K_DOWN:
        nave_j.movimento_down = True

def check_keyup_events(event, nave_j):
    """Responde a soltura de teclas"""
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            nave_j.movimento_right = False
        elif event.key == pygame.K_LEFT:
            nave_j.movimento_left = False
        elif event.key == pygame.K_UP:
            nave_j.movimento_up = False
        elif event.key == pygame.K_DOWN:
            nave_j.movimento_down = False

def check_eventos(nave_j):
    """Observa eventos de teclado e de mouse"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, nave_j)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, nave_j)

def atualizar_screen(inv_alien, screen, nave_j):
    """Redesenha a tela a cada passagem pelo laço"""
    screen.fill(inv_alien.bg_color)
    nave_j.blitme()

    """Deixa a tela mais recente visível"""
    pygame.display.flip()