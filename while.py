print("Qual seu nome? ")
nome = input()
print("Qual o saldo da sua conta? ")
saldo = float(input())


contador = 0
soma = 0

while saldo > 0:
    saque = int(input('Digite o valor do saque: '))
    if saque == 0:
        print("\nvalor inválido")
        break
    elif saque > saldo:
        print("Não é possível sacar um valor maior que o seu saldo")
        break
    else:
        saldo = saldo - saque
        print("seu saldo é ", saldo)
        contador = contador + 1
        soma = soma + saque 
print('Saldo insuficiente')

"\n"
print("seu nome é ",nome)
print("Você fez ",contador, " saques")
print("O valor total sacado foi ",soma)
print("seu saldo é ",saldo)

