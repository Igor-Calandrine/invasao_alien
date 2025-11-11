"""Check_events()
    Iremos transferir o código que administra eventos para uma função seprada chamada check_events(). Isso simplificará run_game e isolará o laco de gerenciamentoo de eventos. Isolar o laço de eventos permite administrar de forma separada de outros aspectos do jogo, por exemplo a atualização de tela."""

import sys
import pygame
from configuracoes import Configurações
from nave import Nave
import funcoes as funcoes

def run_game():
    """Inicialização e cria objeto para a tela"""
    pygame.init() 

    inv_alien = Configurações()

    screen = pygame.display.set_mode((inv_alien.screen_width, inv_alien.screen_height)) 
    pygame.display.set_caption("Alien Super Invasion")

    """Cria uma nave"""
    nave_j = Nave(screen)

    """Inicia o laço principal do jogo"""
    while True:
        
        funcoes.check_eventos() #função importada
        funcoes.atualizar_screen(inv_alien, screen, nave_j)

run_game()





