#!/usr/bin/env python3

#   0      1      2      3       4       5      6      7    8
# Email  Bills Broncos 49ers Seahawks Texans Patriots Rams Bears
#         30     33

ARQUIVO_ENTRADA = "/home/mrobles/bolao_nfl_2026/palpites_divisional.txt"
DELIMITADOR = "|"


def verifica_resultado(palpite_vencedor, palpite_perdedor, vencedor, perdedor):

    try:
        palpite_vencedor = int(palpite_vencedor)
        palpite_perdedor = int(palpite_perdedor)
        vencedor = int(vencedor)
        perdedor = int(perdedor)
    except ValueError:
        print(f"Valores inválidos")
        return
    
    pontos = 0
    
    #verifica se acertou pontuação máxima do jogo, se não, verifica pontuações individuais
    if palpite_vencedor == vencedor and palpite_perdedor == perdedor:
        pontos = pontos + 30
    else:
        #verifica se acertou vencedor
        if palpite_vencedor > palpite_perdedor:
            pontos = pontos + 10 
        
        #verifica se acertou diferença
        if palpite_vencedor > palpite_perdedor:
            palpite_diferenca = palpite_vencedor - palpite_perdedor
        else:
            palpite_diferenca = palpite_perdedor - palpite_vencedor

        if palpite_diferenca == vencedor - perdedor:
            pontos = pontos + 5

        #verifica se acertou placar do vencedor
        if palpite_vencedor == vencedor:
            pontos = pontos + 5

        #verifica se acertou placar do perdedor
        if palpite_perdedor == perdedor:
            pontos = pontos + 5
    
    # Adicional Multiplicador da rodada antes de retornar a pontuação
    return pontos * 1.5    

def processar_arquivo():
    with open(ARQUIVO_ENTRADA, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip()

            # Ignora linhas vazias
            if not linha:
                continue

            campos = linha.split(DELIMITADOR)

            # Rams x Panthers
            pontos = verifica_resultado(
                campos[2], #vencedor Broncos
                campos[1], #perdedor Bills
                33,
                30
            )

            print(f"Jogo 1 - Bills 30 x 33 Broncos. Usuario {campos[0]} fez { pontos } pontos. |Bills vs Broncos|{campos[0]}|{pontos}") 

if __name__ == "__main__":
    processar_arquivo()

