import pygame

class Nave():

    def __init__(self, screen):
        """Inicializa a nave e define sua posição inicial"""
        self.screen = screen

        """Carrega a imagem da espaçonave e obtém seu rect"""
        self.imagem = pygame.image.load("Projetos\invasao_alien\imagens\\nave_j.png") #a
        self.imagem = pygame.transform.scale(self.imagem, (50, 50))
        self.rect = self.imagem.get_rect() #c
        self.screen_rect = screen.get_rect()

        """Inicia cada nova nave na porte inferior central da tela"""
        self.rect.centerx = self.screen_rect.centerx #b
        self.rect.bottom = self.screen_rect.bottom #b

    def blitme(self):
        """Desenha a nave em sua posição inicial"""
        self.screen.blit(self.imagem, self.rect) #d

"""A referência dos parâmetros é para referência a tela em mque desenharemos a espaçonave."""

#a, aqui chamamos a imagem e armazenada em #self.imagem
#b, posição da por nome, muito parecido com CSS. Pode-se especificar com eixo x e y
#c, cria o retângulo que envolve a imagem
#d, desenha a nave usando rect

"""Um dos motivos de Pygamer ser tão eficiente é que ele poermite tratar elementos do jogo como retângulos (rects), mesmo que eles não tenham exatamente o formato de um retângulo

O método blitme() é criado pelo desenvolvedor, normalmente aparece dentro de uma classe para organizar o código e chamar o blit() internamente.
blit() → Desenha uma imagem em uma superfície
"""

