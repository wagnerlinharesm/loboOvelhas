    #!/usr/bin/env python3
# -*- codificacao: utf-8 -*-
"""
Created on Sun Sep 23 15:33:59 2018
@author: talles medeiros, decsi-ufop
"""

"""
Este código servirá de exemplo para o aprendizado do algoritmo MINIMAX 
na disciplina de Inteligência Artificial - CSI457
Semestre: 2018/2
"""

# !/usr/bin/env python3
from math import inf as infinity
from random import choice
import platform
import time
from os import system

"""
Um versão simples do algoritmo MINIMAX para o Jogo da Velha.
"""

# Representando a variável que identifica cada jogador
# HUMANO = Oponente humano
# COMP = Agente Inteligente
# tabuleiro = dicionário com os valores em cada posição (x,y)
# indicando o jogador que movimentou nessa posição.
# Começa vazio, com zero em todas posições.
HUMANO = -1
COMP = +1
from random import randint
lobo = ([7, 4])

ovelha_1 = ([0, 1, 0])
ovelha_2 = ([0, 3, 0])
ovelha_3 = ([0, 5, 0])
ovelha_4 = ([0, 7, 0])

ovelhas = ([0,0,0,0])

tabuleiro = [
    [0, 1, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, -1, 0, 0, 0],
]

"""
Funcao para avaliacao heuristica do estado.
:parametro (estado): o estado atual do tabuleiro
:returna: +1 se o computador vence; -1 se o HUMANOo vence; 0 empate
 """


def avaliacao(estado):
    if vitoria_ovelha(estado, COMP):
        placar = +1
    elif vitoria_lobo(estado, HUMANO):
        placar = -1
    else:
        placar = 0

    return placar


""" fim avaliacao (estado)------------------------------------- """


def vitoria_lobo(estado, jogador):
    """
    Esta funcao testa se um jogador especifico vence. Possibilidades:
    * Tres linhas     [X X X] or [O O O]
    * Tres colunas    [X X X] or [O O O]
    * Duas diagonais  [X X X] or [O O O]
    :param. (estado): o estado atual do tabuleiro
    :param. (jogador): um HUMANO ou um Computador
    :return: True se jogador vence
    """
    win_estado = [
        [estado[0][1]], [estado[0][3]], [estado[0][5]], [estado[0][7]]  # toda linha 1
    ]
    # Se um, dentre todos os alinhamentos pertence um mesmo jogador, 
    # então o jogador vence!
    if [jogador] in win_estado:
        return True
    else:
        return False


def vitoria_ovelha(estado, jogador):
    """
    Esta funcao testa se um jogador especifico vence. Possibilidades:
    * Tres linhas     [X X X] or [O O O]
    * Tres colunas    [X X X] or [O O O]
    * Duas diagonais  [X X X] or [O O O]
    :param. (estado): o estado atual do tabuleiro
    :param. (jogador): um HUMANO ou um Computador
    :return: True se jogador vence
    """
    # win_estado = [
    #     [estado[0][1]], [estado[0][3]], [estado[0][5]], [estado[0][7]] # toda linha 1
    # ]
    # Se um, dentre todos os alinhamentos pertence um mesmo jogador,
    # então o jogador vence!

    cell = celulas_vazias_lobo(estado)

    if cell == []:
        return True
    else:
        return False


""" ---------------------------------------------------------- """

"""
Testa fim de jogo para ambos jogadores de acordo com estado atual
return: será fim de jogo caso ocorra vitória de um dos jogadores.
"""


def fim_jogo(estado):
    return vitoria_lobo(estado, HUMANO) or vitoria_ovelha(estado, COMP)


""" ---------------------------------------------------------- """

"""
Verifica celular vazias e insere na lista para informar posições
ainda permitidas para próximas jogadas.
"""


def celulas_vazias(estado):
    celulas = []
    for x, row in enumerate(estado):
        for y, cell in enumerate(row):
            if cell == 0: celulas.append([x, y])
    return celulas


def celulas_vazias_lobo(estado):
    celulas = []
    for x, row in enumerate(estado):
        for y, cell in enumerate(row):
            if cell == -1:
                if x + 1 < 8 and y + 1 < 8 and estado[x + 1][y + 1] == 0:
                    celulas.append([x + 1, y + 1])
                if x + 1 < 8 and y - 1 >= 0 and estado[x + 1][y - 1] == 0:
                    celulas.append([x + 1, y - 1])
                if x - 1 >= 0 and y - 1 >= 0 and estado[x - 1][y - 1] == 0:
                    celulas.append([x - 1, y - 1])
                if x - 1 >= 0 and y + 1 < 8 and estado[x - 1][y + 1] == 0:
                    celulas.append([x - 1, y - 1])

    return celulas


def celulas_vaziasOvelha(estado):
    celulas = []
    for x, row in enumerate(estado):
        for y, cell in enumerate(row):
            if cell == 1:

                if (x + 1) < 8 and (y - 1) >= 0 and estado[x + 1][y - 1] == 0:
                    celulas.append([x + 1, y - 1])

                if x + 1 < 8 and y + 1 < 8 and estado[x + 1][y + 1] == 0:
                    celulas.append([x + 1, y + 1])

    return celulas


""" ---------------------------------------------------------- """

"""
Um movimento é valido se a célula escolhida está vazia.
:param (x): coordenada X
:param (y): coordenada Y
:return: True se o tabuleiro[x][y] está vazio
"""


def movimento_valido(x, y):
    # movimentos = {
    #     1: [ovelha1[0] + 1, ovelha1[1] - 1], 2: [ovelha1[0] + 1, ovelha1[1] + 1],
    # }
    if [x, y] in celulas_vaziasOvelha(tabuleiro):
        # if [x, y] in movimentos:
        return True
    else:
        return False


def movimento_validoLobo(x, y):
    if [x, y] in celulas_vazias(tabuleiro):
        tabuleiro[lobo[0]][lobo[1]] = 0
        return True
    else:
        return False


""" ---------------------------------------------------------- """

"""
Executa o movimento no tabuleiro se as coordenadas são válidas
:param (x): coordenadas X
:param (y): coordenadas Y
:param (jogador): o jogador da vez
"""


def exec_movimento(x, y, jogador):
    if movimento_valido(x, y):

        if (x == (ovelha_2[0] + 1) and y == (ovelha_2[1] + 1)) or (
                x == (ovelha_2[0] + 1) and y == (ovelha_2[1] - 1)):
            # ovelha_2[2] = 1
            ovelhas[1] = 1

        if (x == (ovelha_1[0] + 1) and y == (ovelha_1[1] + 1)) or (
                x == (ovelha_1[0] + 1) and y == (ovelha_1[1] - 1)):
            #ovelha_1[2] = 1
            ovelhas[0] = 1

        if (x == (ovelha_3[0] + 1) and y == (ovelha_3[1] + 1)) or (
                x == (ovelha_3[0] + 1) and y == (ovelha_3[1] - 1)):
         #  ovelha_3[2] = 1
           ovelhas[2] = 1

        if (x == (ovelha_4[0] + 1) and y == (ovelha_4[1] + 1)) or (
                x == (ovelha_4[0] + 1) and y == (ovelha_4[1] - 1)):
           #  ovelha_4[2] = 1
            ovelhas[3] = 1

        ov = False

        while ov == False:
            k = randint(0, 3)

            if (ovelhas[k] == 1):

                if (k == 0):
                    ovelha_1[2] = 1
                elif (k == 1):
                    ovelha_2[2] = 1
                elif (k == 2):
                    ovelha_3[2] = 1
                elif (k == 3):
                    ovelha_4[2] = 1
                for i in range(4):
                    ovelhas[i] = 0

                ov = True

        if ovelha_1[2] == 1:
            tabuleiro[ovelha_1[0]][ovelha_1[1]] = 0
            ovelha_1[0] = x
            ovelha_1[1] = y
            ovelha_1[2] = 0

        elif ovelha_2[2] == 1:
            tabuleiro[ovelha_2[0]][ovelha_2[1]] = 0
            ovelha_2[0] = x
            ovelha_2[1] = y
            ovelha_2[2] = 0

        elif ovelha_3[2] == 1:
            tabuleiro[ovelha_3[0]][ovelha_3[1]] = 0
            ovelha_3[0] = x
            ovelha_3[1] = y
            ovelha_3[2] = 0

        elif ovelha_4[2] == 1:
            tabuleiro[ovelha_4[0]][ovelha_4[1]] = 0
            ovelha_4[0] = x
            ovelha_4[1] = y
            ovelha_4[2] = 0

        tabuleiro[x][y] = jogador
        # tabuleiro[loboX][loboY] = 0

        return True
    else:
        return False


def exec_movimentoLobo(x, y, jogador):
    if movimento_validoLobo(x, y):
        tabuleiro[x][y] = jogador
        lobo[0] = x
        lobo[1] = y

        return True
    else:
        return False


""" ---------------------------------------------------------- """

"""
Função da IA que escolhe o melhor movimento
:param (estado): estado atual do tabuleiro
:param (profundidade): índice do nó na árvore (0 <= profundidade <= 9),
mas nunca será nove neste caso (veja a função iavez())
:param (jogador): um HUMANO ou um Computador
:return: uma lista com [melhor linha, melhor coluna, melhor placar]
"""


def minimax(estado, profundidade, jogador):
    # valor-minmax(estado)
    if jogador == COMP:
        melhor = [-1, -1, -infinity]
    else:
        melhor = [-1, -1, +infinity]

    # valor-minimax(estado) = avaliacao(estado)
    if profundidade == 0 or fim_jogo(estado):
        placar = avaliacao(estado)
        return [-1, -1, placar]
    if jogador == COMP:
        for cell in celulas_vaziasOvelha(estado):
            x, y = cell[0], cell[1]

            estado[x][y] = jogador
            placar = minimax(estado, profundidade - 1, -jogador)
            estado[x][y] = 0
            placar[0], placar[1] = x, y

            if jogador == COMP:
                if placar[2] > melhor[2]:
                    melhor = placar  # valor MAX
            else:
                if placar[2] < melhor[2]:
                    melhor = placar  # valor MIN
    elif jogador == HUMANO:
        for cell in celulas_vazias(estado):
            x, y = cell[0], cell[1]

            estado[x][y] = jogador
            placar = minimax(estado, profundidade - 1, -jogador)
            estado[x][y] = 0
            placar[0], placar[1] = x, y

            if jogador == COMP:
                if placar[2] > melhor[2]:
                    melhor = placar  # valor MAX
            else:
                if placar[2] < melhor[2]:
                    melhor = placar  # valor MIN

    return melhor


""" ---------------------------------------------------------- """

"""
Limpa o console para SO Windows
"""


def limpa_console():
    os_name = platform.system().lower()
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')


""" ---------------------------------------------------------- """

"""
Imprime o tabuleiro no console
:param. (estado): estado atual do tabuleiro
"""


def exibe_tabuleiro(estado, comp_escolha, humano_escolha):
    print('----------------------------------------')
    for row in estado:
        print('\n----------------------------------------')
        for cell in row:
            if cell == +1:
                print('|', comp_escolha, '|', end='')
            elif cell == -1:
                print('|', humano_escolha, '|', end='')
            else:
                print('|', ' ', '|', end='')
    print('\n----------------------------------------')


""" ---------------------------------------------------------- """

"""
Chama a função minimax se a profundidade < 9,
ou escolhe uma coordenada aleatória.
:param (comp_escolha): Computador escolhe X ou O
:param (humano_escolha): HUMANO escolhe X ou O
:return:
"""


def IA_vez(comp_escolha, humano_escolha):
    # profundidade = len(celulas_vazias(tabuleiro))
    profundidade = 4
    if profundidade == 0 or fim_jogo(tabuleiro):
        return

    limpa_console()
    print('Vez do Computador [{}]'.format(comp_escolha))
    exibe_tabuleiro(tabuleiro, comp_escolha, humano_escolha)

    move = minimax(tabuleiro, profundidade, COMP)
    x, y = move[0], move[1]

    exec_movimento(x, y, COMP)
    time.sleep(1)


""" ---------------------------------------------------------- """


def HUMANO_vez(comp_escolha, humano_escolha):
    """
    O HUMANO joga escolhendo um movimento válido
    :param comp_escolha: Computador escolhe X ou O
    :param humano_escolha: HUMANO escolhe X ou O
    :return:
    """
    profundidade = 4
    if profundidade == 0 or fim_jogo(tabuleiro):
        return

    # Dicionário de movimentos válidos
    movimento = -1
    # movimentos = {
    #     1: [0, 0], 2: [0, 1], 3: [0, 2],
    #     4: [1, 0], 5: [1, 1], 6: [1, 2],
    #     7: [2, 0], 8: [2, 1], 9: [2, 2],
    # }
    movimentos = {
        1: [lobo[0] + 1, lobo[1] + 1], 2: [lobo[0] + 1, lobo[1] - 1], 3: [lobo[0] - 1, lobo[1] - 1],
        4: [lobo[0] - 1, lobo[1] + 1],
    }

    limpa_console()
    print('Vez do HUMANO [{}]'.format(humano_escolha))
    exibe_tabuleiro(tabuleiro, comp_escolha, humano_escolha)

    while (movimento < 1 or movimento > 4):
        try:
            movimento = int(input('Use numero (1..4): '))
            coord = movimentos[movimento]
            tenta_movimento = exec_movimentoLobo(coord[0], coord[1], HUMANO)

            if tenta_movimento == False:
                print('Movimento Inválido')
                movimento = -1


        except KeyboardInterrupt:
            print('Tchau!')
            exit()
        except:
            print('Escolha Inválida!')


""" ---------------------------------------------------------- """

"""
Funcao Principal que chama todas funcoes
"""


def main():
    limpa_console()
    humano_escolha = 'L'  # Pode ser X ou O
    comp_escolha = 'O'  # Pode ser X ou O

    primeiro = 'S'  # se HUMANO e o primeiro

    # # HUMANO escolhe X ou O para jogar
    # while humano_escolha != 'O' and humano_escolha != 'X':
    #     try:
    #         print('')
    #         humano_escolha = input('Escolha X or O\n: ').upper()
    #     except KeyboardInterrupt:
    #         print('Tchau!')
    #         exit()
    #     except:
    #         print('Escolha Errada')
    #
    # # Setting Computador's choice
    # if humano_escolha == 'X':
    #     comp_escolha = 'O'
    # else:
    #     comp_escolha = 'X'

    # HUMANO pode começar primeiro
    limpa_console()
    while primeiro != 'S' and primeiro != 'N':
        try:
            primeiro = input('Primeiro a Iniciar?[s/n]: ').upper()
        except KeyboardInterrupt:
            print('Tchau!')
            exit()
        except:
            print('Escolha Errada!')

    # Laço principal do jogo
    while len(celulas_vazias(tabuleiro)) > 0 and not fim_jogo(tabuleiro):
        if primeiro == 'N':
            IA_vez(comp_escolha, humano_escolha)
            primeiro = ''

        HUMANO_vez(comp_escolha, humano_escolha)
        IA_vez(comp_escolha, humano_escolha)

    # Mensagem de Final de jogo
    if vitoria_lobo(tabuleiro, HUMANO):
        limpa_console()
        print('Vez do HUMANO [{}]'.format(humano_escolha))
        exibe_tabuleiro(tabuleiro, comp_escolha, humano_escolha)
        print('Você Venceu!')
    elif vitoria_ovelha(tabuleiro, COMP):
        limpa_console()
        print('Vez do Computador [{}]'.format(comp_escolha))
        exibe_tabuleiro(tabuleiro, comp_escolha, humano_escolha)
        print('Você Perdeu!')
    else:
        limpa_console()
        exibe_tabuleiro(tabuleiro, comp_escolha, humano_escolha)
        print('Empate!')

    exit()


if __name__ == '__main__':
    main()
