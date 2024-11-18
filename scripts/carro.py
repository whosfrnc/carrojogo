import pygame

class Carro:
    def __init__(self, tela, x, y):
        self.tela = tela
        # Carregar a imagem do carro e definir o tamanho
        self.imagem = pygame.image.load('assets/carro.png')
        self.tamanho = (50, 30)  # Definir o tamanho do carro (largura, altura)
        self.imagem = pygame.transform.scale(self.imagem, self.tamanho)
        
        self.posicao = [x, y]
        self.rect = self.imagem.get_rect(topleft=self.posicao)  # Define a posição inicial do carro

    def desenhar(self):
        # Desenhar a imagem do carro na tela
        self.tela.blit(self.imagem, self.posicao)

    def atualizar(self):
        # Lógica de movimento
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_UP]:  # Pressione a tecla 'up' para subir
            self.posicao[1] -= 5  # Mover para cima por 5 pixels
        if teclas[pygame.K_DOWN]:  # Pressione a tecla 'down' para descer
            self.posicao[1] += 5  # Mover para baixo por 5 pixels
        if teclas[pygame.K_RIGHT]:  # Pressione a tecla 'right' para mover para a direita
            self.posicao[0] += 5  # Mover para a direita por 5 pixels
        if teclas[pygame.K_LEFT]:  # Pressione a tecla 'left' para mover para a esquerda
            self.posicao[0] -= 5  # Mover para a esquerda por 5 pixels

        # Limitar o movimento do carro à tela
        largura_tela, altura_tela = self.tela.get_size()
        if self.posicao[0] < 0:
            self.posicao[0] = 0
        if self.posicao[0] > largura_tela - self.tamanho[0]:
            self.posicao[0] = largura_tela - self.tamanho[0]
        if self.posicao[1] < 0:
            self.posicao[1] = 0
        if self.posicao[1] > altura_tela - self.tamanho[1]:
            self.posicao[1] = altura_tela - self.tamanho[1]

        # Atualizar o retângulo do carro
        self.rect = pygame.Rect(self.posicao, self.tamanho)

    def getRect(self):
        return self.rect
