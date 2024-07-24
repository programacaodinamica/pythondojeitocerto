import getpass

EMPATE = 0
VIT_JOGADOR1 = 1
VIT_JOGADOR2 = 2

def pre_processar_resposta(escolha):
    return escolha.lower().strip()

def solicitar_escolhas():
    escolhas = []
    for i in range(1, 3):
        escolha = getpass.getpass(f"Jogador {i} - Escolha 'pedra', 'papel' ou 'tesoura': ")
        escolhas.append(pre_processar_resposta(escolha))
    return escolhas

def jokenpo(jogador1, jogador2):
    if jogador1 == jogador2:
        return EMPATE
    elif ((jogador1 == 'pedra' and jogador2 == 'tesoura') or
        (jogador1 == 'tesoura' and jogador2 == 'papel') or
        (jogador1 == 'papel' and jogador2 == 'pedra')):
        return VIT_JOGADOR1
    else:
        return VIT_JOGADOR2

escolhas = solicitar_escolhas()
resultado = jokenpo(escolhas[0], escolhas[1])

print("\n-----------: ")
for i, escolha in enumerate(escolhas):
    print(f"Jogador {i+1}: {escolha}.")   
print("\nRESULTADO: ")
if resultado == EMPATE:
    print("Empate")
elif resultado == VIT_JOGADOR1:
    print("JOGADOR 1 venceu!")
else:
    print("JOGADOR 2 venceu!")

