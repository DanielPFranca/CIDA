notas = [6,8,10,7,9]
soma = 0
x = 0
while x<5:
    soma += notas[x]
    x = x+1
print("Média: %5.2f" % (soma/x))
#####################################################################
notas = [0,0,0,0,0]
soma = 0
x = 0

while x < 5:
    notas[x] = float(input("Nota %d" % x))
    soma += notas[x]
    x = x + 1
x = 0
while x < 5:
    print("Nota %d: %6.2f" % (x, notas[x]))
    x = x + 1
print("Média: %5.2f" % (soma/x))
#####################################################################

numeros = [0,0,0,0,0]
x = 0

while x < 5:
    numeros[x] = int(input("Número %d:" % (x+1)))
    x += 1
while True:
    escolhido = int(input("Qual a posição deseja visualizar? (0 -> sair):"))
    if escolhido == 0:
        break
    print("Número escolhido: %d" % (numeros[escolhido - 1]))

#####################################################################

l = [10,20,30,40,50]
v = l[:]
v[0] = 60
print(l, v)
#####################################################################
l = [1,2,3,4,5]
y = l[2:5]
x = l[:-1]
z = l[3:]
print(x, y, z)

a = [12, 9, 5]
b = len(a)
print(b)
#####################################################################
l = [1,2,3]
x = 0
while x < 3:
    print(l[x])
    x = x + 1


#####################################################################
l = [1,2,3]
x = 0
while x < len(l):
    print(l[x])
    x = x + 1

l.append(4)
l.append(5)
print(l)

y = len(l)
print(y)
#####################################################################
l = []
while True:
    n = int(input("Digite um número (0 sai): "))
    if n == 0:
        break
    l.append(n)
x = 0
while x < len(l):
    print(l[x])
    x = x + 1

#####################################################################
l = []
l = l+[1, 2, 3, 4]

print(l)
#####################################################################
l = ["a", "b"]
l.append(["c", "d"])
print(l)
l.extend(["f", "g", "h"])
print(l[2][1])
#####################################################################
l = ["a", "b", "c"]
del l[1]
print(l)

del l[0]
print(l)
#####################################################################
l = list(range(101))
print(l)

del l[1:99]
print(l)
#####################################################################
FIFO

ultimo = 10
fila = list(range(1, ultimo + 1))
while True:
    print("\nExixtem %d clientes na fila" % len(fila))
    print("Fila atual:", fila)
    print("Digite F para adicionar ao fim da fila,")
    print("ou A para realizar o atendimento. S para sair.")
    operacao = input("Operação (F, A ou S):")

    if operacao == "A":
        if(len(fila)) > 0:
            atendido = fila.pop(0)
            print("Cliente %d atendido" % atendido)
        else:
            print("Fila vazia! Nimguém para atender.")
    elif operacao == "F":
        ultimo +=1 # Incrementa o ticket do novo cliente
        fila.append(ultimo)
    elif operacao == "S":
        break
    else:
        print("Operação inválida! Digite apenas F, A ou S!")

#####################################################################
prato = 5
pilha = list(range(1, prato + 1))
while True:
    print("\nExixtem %d pratos na pilha" % len(pilha))
    print("Pilha atual:", pilha)
    print("Digite E para para empilhar um novo prato,")
    print("ou D para desempilhar. S para sair.")
    operacao = input("Operação (E, D ou S):")

    if operacao == "D":
        if (len(pilha)) > 0:
            atendido = pilha.pop()
            print("Prato %d lavado" % atendido)
        else:
            print("Pilha vazia! Nenhum para lavar.")
    elif operacao == "E":
        prato += 1
        pilha.append(prato)
    elif operacao == "S":
        break
    else:
        print("Operação inválida! Digite apenas F, A ou S!")

######################################################################


l = [15,7,27,39]
p = int(input("Digite o valor a procurar:"))
achou = False
x = 0
while x < len(l):
    if l[x] == p:
        achou = True
        break
    x = x + 1
if achou:
    print("%d achado na posição %d" % (p,x))
else:
    print("%d não encontrado" % p)




