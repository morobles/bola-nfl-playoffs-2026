#!/usr/bin/env python3

# Bears 31 - 27 Packers
# Panthers 31 - 34 Rams
# Jaguars 24 - 27 Bills
#   0     1      2       3      4     5      6      7      8       9       10      11      12
# email Rams Panthers Packers Bears Bills Jaguars 49ers Eagles Chargers Patriots Texans Steelers
#        34     31       27    31    27     24     23     19       3       16      30      6

ARQUIVO_ENTRADA = "/home/mrobles/bolao_nfl_2026/palpites_wildcard.txt"
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

    return pontos    

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
                campos[1], #vencedor Rams
                campos[2], #perdedor Panthers
                34,
                31
            )

            print(f"Jogo 1 - Rams 34 x 31 Panthers. Usuario {campos[0]} fez { pontos } pontos. |Rams x Panthers|{campos[0]}|{pontos}") 

            # Packers x Bears
            pontos = verifica_resultado(
                campos[4], #vencedor Bears
                campos[3], #perdedor Packers
                31,
                27
            )

            print(f"Jogo 2 - Packers 27 x 31 Bears. Usuario {campos[0]} fez { pontos } pontos. |Packers vs Bears|{campos[0]}|{pontos}") 

            # Bills x Jaguars
            pontos = verifica_resultado(
                campos[5], #vencedor Bills
                campos[6], #perdedor Jaguars
                27,
                24
            )   
            
            print(f"Jogo 3 - Bills 27 x 24 Jaguarss. Usuario {campos[0]} fez { pontos } pontos. |Bills vs Jaguars|{campos[0]}|{pontos}")

            # 49ers x Eagles
            pontos = verifica_resultado(
                campos[7], #vencedor 49ers
                campos[8], #perdedor Eagles
                23,
                19
            )

            print(f"Jogo 4 - 49ers 23 x 19 Eagles. Usuario {campos[0]} fez { pontos } pontos. |49ers vs Eagles|{campos[0]}|{pontos}")

            # Chargers x Patriots
            pontos = verifica_resultado(
                campos[10], #vencedor Patriots
                campos[9], #perdedor Chargers
                16,
                3
            )

            print(f"Jogo 5 - Chargers 3 x 16 Patriots. Usuario {campos[0]} fez { pontos } pontos. |Chargers vs Patriots|{campos[0]}|{pontos}")

            # Chargers x Patriots
            pontos = verifica_resultado(
                campos[11], #vencedor Texans
                campos[12], #perdedor Steelers
                30,
                6
            )

            print(f"Jogo 6 - Texans 30 x 6 Steelers. Usuario {campos[0]} fez { pontos } pontos. |Texans vs Steelers|{campos[0]}|{pontos}")

if __name__ == "__main__":
    processar_arquivo()

