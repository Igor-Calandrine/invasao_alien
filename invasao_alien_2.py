"""Agora, após escrever a classe da nave, iremos desenhá-la no jogo importando sua classe"""

import sys
import pygame
from configuracoes import Configurações
from nave import Nave

def run_game():
    """Inicialização e cria objeto para a tela"""
    pygame.init() 

    inv_alien = Configurações()

    screen = pygame.display.set_mode((inv_alien.screen_width, inv_alien.screen_height)) 
    pygame.display.set_caption("Alien Super Invasion")

    """Cria uma nave"""
    nave_j = Nave(screen) #a

    """Inicia o laço principal do jogo"""
    while True:
        
        """Observa eventos de teclado e de mouse"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        """Redesenha a tela a cada passagem pelo laço"""
        screen.fill(inv_alien.bg_color)
        nave_j.blitme() #b

        """Deixa a tela mais recente visível"""
        pygame.display.flip()

run_game()

#a, importamos a classe criamos um instância de Nave para guardar sua configurações.
#b, foi chamado o método para preencher a cor de fundo com a nave sobre a cor da tela.




