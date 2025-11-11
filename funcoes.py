import sys
import pygame

def check_eventos():
    """Observa eventos de teclado e de mouse"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def atualizar_screen(inv_alien, screen, nave_j):
    """Redesenha a tela a cada passagem pelo laço"""
    screen.fill(inv_alien.bg_color)
    nave_j.blitme()

    """Deixa a tela mais recente visível"""
    pygame.display.flip()