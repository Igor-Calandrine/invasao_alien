"""
Respondendo a um repssionamento de tecla
    Sempre que o jogador pressionar uma tecla, esse pressionamento será registrado no Pygame como um evento. Todo evento é capturado pelo método pygame.event.get(), portanto precisamos especificar quais são os tipos de eventos que queremos verificar em nossa função check_eventos().
    
    Todo pressionamento de tecla é registrado como um evento KEYDOWN.
    
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            #Move a nave para a direita
            ship.rect.centerx += 1
            
Movimento Contínuo
    Faremos nosso jogo detectar um evento #pygamer.KEYUP para que possamos saber quando a seta para a direita foi solta. Quando a nave estiver parada, a flag moving_right será False. Quando a seta para a direita for pressionada, definiremos a flag como True.
    
    Na classe Nave então teremos:
    
    #Flag de movimento
    self.movimento_right = False
    
    def atualizar(self):
        #Atualiza a posição da espaçonave de acordo com a flag de movimento
        # if self.movimento_right:
        # self.rect.centerx += 1
        
Ajustando a velocidade
    Vamos acrescentar um controle na velocidade da nave com o atributo nave_fator_velocidade na classe de Configurações. Quando quisermos mover a nave ajustaremos sua posição 1,5 pixel e não 1 pixel. No entando, os atrobutos de retângulo como centerx amazenam apenas valores inteiros, portanto precisamos fazer algumas modificações em Nave como acrescentar a função float.
    
    #Configurações da nave
    self.nave_fator_velocidade = 1.5
    
Limitando o alcance da espaçonave
    A nave agora está desaparecendo nas bordas da tela. Vamos agora limitar sua posição até o limite da tela.
        if self.moving_right and self.rect.right < self.screen_rect.right
        if self.moving_right and self.rect.right > 0
    """

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
    nave_j = Nave(screen, inv_alien)

    """Inicia o laço principal do jogo"""
    while True:
        
        funcoes.check_eventos(nave_j)
        nave_j.atualizar()
        funcoes.atualizar_screen(inv_alien, screen, nave_j)

run_game()





