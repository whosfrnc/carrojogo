import pygame
from scripts.cenas import *



pygame.init()

tamanhoTela = [600,400]
tela = pygame.display.set_mode(tamanhoTela)
pygame.display.set_caption("Jogo Franco Carro")
relogio = pygame.time.Clock()
corFundo = (86, 148, 214)


listaCenas = {
    'partida' : Partida(tela),
    'menu' : Menu(tela)
}

cenaAtual = 'menu'

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()

    tela.fill(corFundo)

    cenaAtual = listaCenas[cenaAtual].atualizar()


    relogio.tick(60)
    pygame.display.flip()