import pygame
from scripts.cone import Cone
from scripts.carro import Carro
from scripts.interface import Texto, Botao

class Partida:
    def __init__(self, tela):
        self.tela = tela
        largura, altura = self.tela.get_size()  # Obtendo tamanho da tela

        # Carregando e redimensionando a imagem de fundo
        self.fundo = pygame.image.load('assets/estrada.png')  # Carregando a imagem
        self.fundo = pygame.transform.scale(self.fundo, (largura, altura))  # Redimensionando a imagem

        self.carro = Carro(tela, 100, 300)  # Posição inicial do carro
        self.cones = [Cone(tela) for _ in range(18)]  # Criando 18 cones
        self.estado = "partida"
        self.pontosValor = 0
        self.contador = 0
        self.pontosTexto = Texto(tela, str(self.pontosValor), 10, 10, (255, 255, 255), 30)

    def atualizar(self):
        # Desenhar a imagem de fundo
        self.tela.blit(self.fundo, (0, 0))
        self.estado = "partida"
        self.carro.atualizar()

        # Atualiza cada cone
        for cone in self.cones:
            cone.atualizar()

        # Verifica a colisão com cada cone
        for cone in self.cones:
            if cone.detectarColisao(self.carro.rect):
                self.estado = "menu"
                self.carro.posicao = [100, 300]
                self.cones = [Cone(self.tela) for _ in range(10)]  # Reinicia os cones
                return self.estado  # Retorna ao menu se colidir

        # Remove cones que saíram da tela e adiciona novos
        self.cones = [cone for cone in self.cones if cone.x + cone.imagem.get_width() > 0]
        while len(self.cones) < 18:
            novo_cone = Cone(self.tela)
            self.cones.append(novo_cone)

        self.carro.desenhar()
        for cone in self.cones:
            cone.desenhar()

        # Atualizando a pontuação
        self.contador += 1
        if self.contador > 60:
            self.pontosValor += 1
            self.contador = 0
            self.pontosTexto.atualizarTexto(str(self.pontosValor))

        self.pontosTexto.desenhar()
        return self.estado


class Menu:
    def __init__(self, tela):
        self.tela = tela
        largura, altura = self.tela.get_size()  # Obtendo tamanho da tela

        # Carregando e redimensionando a imagem de fundo
        self.fundo = pygame.image.load('assets/estrada.png')  # Carregando a imagem
        self.fundo = pygame.transform.scale(self.fundo, (largura, altura))  # Redimensionando a imagem

        self.titulo = Texto(tela, "Jogo Carrinho", 100, 20, (255, 255, 255), 50)
        self.botao_jogar = Botao(tela, "Jogar", 100, 100, 50, (200, 0, 0), (255, 255, 255))
        self.estado = "menu"

    def atualizar(self):
        # Desenhar a imagem de fundo
        self.tela.blit(self.fundo, (0, 0))
        self.titulo.desenhar()
        self.botao_jogar.desenhar()

        if self.botao_jogar.get_click():
            self.estado = "partida"

        return self.estado
