from random import randint

n1 = int(input('Numero 1: '))
n2 = int(input('Numero 2: '))
n3 = int(input('Numero 3: '))

numeros = [n1, n2, n3]
numeros . sort()

print(f'Numeros em forma ordenada (crescente): {numeros}')

nomeUsu = str(input('Digite o seu nome: '))
print(f'Boas vindas {nomeUsu}')

numAleaPc = randint(0,10)

numEscolhaUsu = int(input('Escolha 1 (ÍMPAR) ou 2 (PAR): '))

numUsu = int(input('Digite um numero: '))

soma = numAleaPc + numUsu
resto = soma % 2

if resto == 1 and numEscolhaUsu == 1:
    print(f'O numero e impar: VENCEDOR {nomeUsu}')
elif resto == 0 and numEscolhaUsu == 2:
    print(f'O numero e par: VENCEDOR {nomeUsu}')
elif resto == 1:
    print('O numero e impar: VENCEDOR PC')
else:
    print(f'O numero e par: VENCEDOR PC')   
print("Fim")
