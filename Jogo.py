import pygame
import time
import random
pygame.init()
largura = 900
altura = 700
configTela = (largura, altura)
gameDisplay = pygame.display.set_mode(configTela)
clock = pygame.time.Clock()
black = (0, 0, 0)
white = (255, 255, 255)
pygame.display.set_caption("3,2,1 Frita Batatinha")
icone = pygame.image.load("JOGUIMPROGRAMACAO/assets/squidgame.png")
ironMan = pygame.image.load("JOGUIMPROGRAMACAO/assets/veio1.png")
pygame.display.set_icon(icone)
larguraIronMan = 100
fundo = pygame.image.load("JOGUIMPROGRAMACAO/assets/sky.png")
missel = pygame.image.load("JOGUIMPROGRAMACAO/assets/boladegude.png")
explosaoSound = pygame.mixer.Sound("JOGUIMPROGRAMACAO/assets/fimround6.wav")
misselSound = pygame.mixer.Sound("JOGUIMPROGRAMACAO/assets/somroun6.wav")
explosaoSound.set_volume(1.5)
misselSound.set_volume(0.2)
def mostraIron(x, y):
    gameDisplay.blit(ironMan, (x, y))
def mostraMissel(x, y):
    gameDisplay.blit(missel, (x, y))
def text_objects(texto, font):
    textSurface = font.render(texto, True, black)
    return textSurface, textSurface.get_rect()
def escreverTela(texto):
    fonte = pygame.font.Font("freesansbold.ttf", 115)
    TextSurf, TextRect = text_objects(texto, fonte)
    TextRect.center = ((largura/2, altura/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(5)
    game()
def escreverPlacar(contador):
    fonte = pygame.font.SysFont(None, 30)
    texto = fonte.render("Desvios:"+str(contador), True, black)
    gameDisplay.blit(texto, (10, 10))
def dead():
    pygame.mixer.Sound.play(explosaoSound)
    pygame.mixer.music.stop()
    escreverTela("Eliminado!")
def game():
    pygame.mixer.music.load("JOGUIMPROGRAMACAO/assets/trilharound6.wav")
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(loops=-1)
    ironPosicaoX = largura*0.42
    ironPosicaoY = altura*0.84
    movimentoX = 0
    velocidade = 20
    misselAltura = 100
    misselLargura = 50
    misselVelocidade = 3
    misselX = random.randrange(0, largura)
    misselY = -200
    desvios = 0
    pygame.mixer.Sound.play(misselSound)
    while True:
        # pega as ações da tela. Ex.: fechar, click de uma tecla ou do mouse
        acoes = pygame.event.get()  # devolve uma lista de ações
        # [ini] mapeando as ações
        for acao in acoes:
            if acao.type == pygame.QUIT:
                pygame.quit()
                quit()
            if acao.type == pygame.KEYDOWN:
                if acao.key == pygame.K_LEFT:
                    movimentoX = velocidade*-1
                elif acao.key == pygame.K_RIGHT:
                    movimentoX = velocidade
            if acao.type == pygame.KEYUP:
                movimentoX = 0
        # [end] mapeando as ações
        # definindo o fundo do game
        gameDisplay.fill(black)
        gameDisplay.blit(fundo, (0, 0))
        # definindo o fundo do game]
        escreverPlacar(desvios)
        misselY = misselY + misselVelocidade
        mostraMissel(misselX, misselY)
        if misselY > altura:
            misselY = -200
            misselX = random.randrange(0, largura)
            desvios = desvios+1
            misselVelocidade += 0.8
            pygame.mixer.Sound.play(misselSound)
        ironPosicaoX += movimentoX
        if ironPosicaoX < 0:
            ironPosicaoX = 0
        elif ironPosicaoX > largura-larguraIronMan:
            ironPosicaoX = largura-larguraIronMan
        # analise de colisão com o IronMan
        if ironPosicaoY < misselY + misselAltura:
            if ironPosicaoX < misselX and ironPosicaoX+larguraIronMan > misselX or misselX+misselLargura > ironPosicaoX and misselX+misselLargura < ironPosicaoX+larguraIronMan:
                dead()
        # analise de colisão com o IronMan
        mostraIron(ironPosicaoX, ironPosicaoY)
        pygame.display.update()
        clock.tick(60)  # faz com que o while execute 60x por segundo
game()
####Mas Que Barbaridade####