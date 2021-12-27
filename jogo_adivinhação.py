from random import randint

inicio = 0
fim = 20

print("======== JOGO ADIVINHAÇÃO DE NÚMEROS ========")
sorteado = randint(inicio,fim)
chute = 0
contagem = 0   #variavel contadora

print(f"Chute um valor entre {inicio} e {fim}:\n")

while chute != sorteado:
    contagem += 1     #incremento a nova jogada
    chute = int(input("Chute:"))
    if (chute == sorteado):
        print(f"Você acertou após {contagem} tentativas!")
    elif (chute > sorteado):
        print("O chute está ACIMA do valor sorteado\n")
    else:   #chute < sorteado
        print("o chute está ABAIXO do valor sorteado\n")

print("Fim do jogo!")