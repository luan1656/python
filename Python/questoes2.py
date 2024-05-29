1 - Liste uma sequência de 10 números do maior para o menor.

n1 = 1
while n1 <= 10:
    print(n1)
    n1 +=1




2 - liste uma sequência numérica que começa em um valor inserido pelo usuário e acaba em um outro valor escolhido pelo usuário

n1 = int(input("insira o primeiro numero: "))
n2 = int(input("insira o ultimo numero: "))

while n1 <= n2:
    print(n1)
    n1 +=1



3 -Solicite um número ao usuário e imprima a tabuada desse número, de 1 a 10

n1 = int(input("Insira um número: "))
for i in range(1, 11):
    print("{} X {} = {} ".format (n1,i,n1*i))





4 -Solicite dois números ao usuário e verifique quantos números pares ou ímpares existem entre esses dois números.

n1 = int(input("insira o primeiro numero: "))
n2 = int(input("insira o ultimo numero: "))

while n1 <= n2:
    
    n1 +=1
    
    if(n1 % 2 == 0):
        print("o número ", n1, " é par")
    
    else:
        print("o número ", n1, " é impar")





5 - Solicite um número inteiro positivo N ao usuário e calcule a soma dos primeiros N números naturais.

soma = 0
n1 = int(input("Insira um número: "))
for rapaz in range(1, n1+1):
    soma+=rapaz
    print(rapaz)
    
print("A soma dos números naturais é: ", soma)



6 - Solicite ao usuário a quantidade de notas que ele deseja inserir, em seguida, solicite essas notas e calcule a média.

soma = 0
media = 0
n1 = int(input("quantas notas deseja inserir: "))

for i in range(1, n1+1):
    nota = float(input('Insira sua {} nota: '.format(i)))
    soma+=nota
    
media = soma / n1

print(media)

# O n1 pede a quantidade de notas que o usuario quer inserir
# O for está pegando a quantidade que usuario deseja e colocando toda vez mais um até chegar na quantidade que o usuario deseja.
# A linha nove está fazendo a conta para chegar na média




7 - Solicite um número inteiro positivo ao usuário e calcule o fatorial desse número.

soma = 1
n1 = int(input("Insira um número: "))
for i in range(1, n1+1):
    soma*=i
    print(i)
    
print("O calculo fatorial é: ", soma)




8 -Desenvolva um programa em Python que permita ao usuário escolher um número e gere a tabuada desse número até um limite especificado pelo próprio usuário.

n1 = int(input("Insira um número: "))
n2 = int(input("insira o resultado limite: "))
for i in range(1, n2+1):
    print("{} X {} = {}".format (n1, i, n1*i))



9 - Desenvolva um programa em Python que solicite ao usuário um número inteiro. O programa deverá então exibir a tabuada de multiplicação até o número escolhido pelo usuário, fazendo as multiplicações de 1 até 10.


n1 = int(input("Insira um número: "))
for i in range(1,n1+1):
    print('Sua tabuada é do {}'.format(i))
    for y in range(1, 11):
        print('{} x {} = {}'.format(i,y,i*y))










10 - Crie um programa em python que faça um triângulo da altura que o usuário escolher(Desafio)

alt = int(input("Informe a altura do triangulo: "))
for i in range(alt):
    print(" "*(alt-i)+"*"*(2*i+1))





