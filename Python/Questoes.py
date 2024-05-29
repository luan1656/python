var = [1, 2, 3, 4]
print(‘A soma de todos os valores é: ’, sum(var))


var = [1, 2, 3, 4]
print('Menor valor', min(var))/
print('Maior valor', max(var))


var = [1, 2, 3, 4]
print('A Média é:', sum(var)/len(var))


lista = [1, 2, 3, 4, 5]
pares = sum(1 for i in lista if i % 2 == 0 )
ímpares = len(lista) - pares
print('Pares: ', (pares))
print('Impares: ', (impares))


var = [1, 2, 3, 4]
orde = sorted(var, key=None, reverse=True  )
print('Reverso', (orde))



var = [1, 2, 3, 4, 1, 2, 3, 4]
print('Sem números duplicos: ', set(var))


rapazes = [('Altair',22), ('Larissa',17), ('Bruce',89)]
orde = sorted(rapazes, key=lambda x: x[0])
print('Nomes em ordem alfabetica: ', (orde))


list1 = [1, 2, 3, 4]
list2 = [8, 7, 6, 5]

orde = sorted(list1+list2)
print('Nomes em ordem alfabetica: ', (orde))




lista = [1, 2, 3, 4, 5, 6]
var1 = int(input("Digite o valor que deseja alterar de 1 a 6: "))
novo = int(input("Digite seu valor: "))

var = [novo if i == var1 else i for i in lista]
print(var)

# Primeiro pegamos o valor novo que a pessoa deseja colocar em seguida o valor é alterado de acordo com o var 1 que é o número que será substituído. 





lista = [1, 2, 3, 4, 5]
valor = int(input(“Insira um valor: ”))

resultado = sorted(True, lista(valor)) if valor in lista == valor (True, None) else (False, None)
print(resultado)






















jogo 

import random
rand = random.randint(1, 100)
tentativa = 2

def insira(tentativa):
    n1 = int(input("Insira o seu número: "))
    dados(n1, tentativa)



def dados(n1, tentativa):
    while tentativa < 0:
        print(tentativa)
        tentativa -= 1
        
    
        if ( rand == n1):
            print("Você acertou o número")
            print("")
            
        elif ( rand > n1):
            print("O número é maior")
            print("")
            insira(tentativa)
            
        elif ( rand < n1):
            print("O número é menor")
            print("")
            insira(tentativa)
            
        
insira(tentativa)        
    
    








