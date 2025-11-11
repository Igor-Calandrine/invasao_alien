import sys #a
import pygame
from configuracoes import Configurações

def run_game():
    """Inicialização e cria objeto para a tela"""
    pygame.init() #b

    inv_alien = Configurações() #Salva configurações nessa variável

    screen = pygame.display.set_mode((inv_alien.screen_width, inv_alien.screen_height)) #c
    pygame.display.set_caption("Alien Super Invasion")

    """Inicia o laço principal do jogo"""
    while True: #d
        
        """Observa eventos de teclado e de mouse"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #e
                sys.exit() #a'

        """Redesenha a tela a cada passagem pelo laço"""
        screen.fill(inv_alien.bg_color)

        """Deixa a tela mais recente visível"""
        pygame.display.flip() #f

run_game()

#a, utilizado para fechar o programa em #a'
#b, inicializa configurações de segundo plano
#c, cria a janela com a tupla como referência. Esse evento é redesenhado automaticamente com o laço #for a cada passagem
#d, o jogo será controlado pelo laço while, que também administra as atuaizações de tela.
#e, quando jogador clicar no fechamento de janela, o evento pygame.QUIT será detectado
#f, atyualizará continuamente o display para mostrar novas posições dos elementos e ocultar posições anteriores, criando a ilusão de movimento.

"""Resumindo
pygame.event → é um submódulo do Pygame (uma parte do Pygame que lida com eventos).

Quando você abre uma janela do Pygame, o sistema operacional começa a enviar eventos como:

mover o mouse → MOUSEMOTION
clicar → MOUSEBUTTONDOWN
apertar uma tecla → KEYDOWN
soltar uma tecla → KEYUP
clicar no “X” da janela → QUIT
Esses eventos ficam armazenados em uma fila de eventos (event queue).

.get() → pega todos os eventos que aconteceram desde a última vez que ele foi chamado.
.flip() → atualiza a tela inteira mostrando todas as mudanças que você fez desde o último frame.
.fill() → preenche ums superfície com uma cor sólida"""



