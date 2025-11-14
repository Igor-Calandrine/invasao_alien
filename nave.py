import pygame

class Nave():

    def __init__(self, screen, inv_alien):
        """Inicializa a nave e define sua posição inicial"""
        self.screen = screen
        self.inv_alien = inv_alien

        """Carrega a imagem da espaçonave e obtém seu rect"""
        self.imagem = pygame.image.load("Projetos\invasao_alien\imagens\\nave_j.png") #a
        self.imagem = pygame.transform.scale(self.imagem, (50, 50))
        self.rect = self.imagem.get_rect() #c
        self.screen_rect = screen.get_rect()

        """Inicia cada jogo uma nova nave na porte inferior central da tela"""
        self.rect.centerx = self.screen_rect.centerx #b
        self.rect.bottom = self.screen_rect.bottom #b

        """Armazena um valor decimal para o centro da nava"""
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        """Flag de movimento"""
        self.movimento_right = False
        self.movimento_left = False
        self.movimento_up = False
        self.movimento_down = False
    
    def atualizar(self):
        """Atualiza a posição da espaçonamve de acordo com a flag de movimento"""
        """Atualiza i valor do centro da nave, e não do retângulo"""
        if self.movimento_right == True:
            if self.movimento_right and self.rect.right < self.screen_rect.right:
                self.centerx += self.inv_alien.nave_fator_velocidade
        if self.movimento_left == True:
            if self.movimento_left and self.rect.left > self.screen_rect.left:
                self.centerx -= self.inv_alien.nave_fator_velocidade
        if self.movimento_up == True:
            if self.movimento_up and self.rect.top > self.screen_rect.top:
                self.centery -= self.inv_alien.nave_fator_velocidade
        if self.movimento_down == True:
            if self.movimento_down and self.rect.bottom< self.screen_rect.bottom:
                self.centery += self.inv_alien.nave_fator_velocidade

        """Atualiza o objeto rect de acordo com o self.center"""
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery
        #apesat de self.center ser um float, apenas a parte inteira é passada para self.rect.centerx


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

