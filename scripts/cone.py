import pygame
import random

class Cone:
    def __init__(self, tela):
        self.imagem = pygame.image.load('assets/cone.png')
        self.imagem = pygame.transform.scale(self.imagem, (30, 50))
        self.tela = tela
        self.x = tela.get_width() + random.randint(0, 100)
        self.y = random.randint(100, 300)  # Altura aleatória
        self.velocidade = 5

    def atualizar(self):
        self.x -= self.velocidade  # Movimento para a esquerda
        if self.x < -self.imagem.get_width():
            self.x = self.tela.get_width()
            self.y = random.randint(100, 300)  # Reiniciar em uma nova altura

    def desenhar(self):
        self.tela.blit(self.imagem, (self.x, self.y))

    def detectarColisao(self, rectCarro):
        return pygame.Rect(self.x, self.y, self.imagem.get_width(), self.imagem.get_height()).colliderect(rectCarro)