"""Em vez de acrescentar configurações por todo o código, vamos criar um módulo chamado  settings que contenha uma classe de nome Settings para armazenar todas as configurações em um só lugar. Essa abordagem nos permite passar um objeto de configurações pelo código, em vez de passar várias configurações individuais. Além disso, ela deixa nossas chamadas de função mais simples e facilita modificar a aparência do jogo à medida que nosso projeto cresce"""

class Configurações():
    """Armazenas todas as confugrações de Invasão Alienígena"""

    def __init__(self):
        """Configurações de tela"""
        self.screen_width = 1200
        self.screen_height = 750
        self.bg_color = (230, 230, 230)

        self.nave_fator_velocidade = 0.5

        