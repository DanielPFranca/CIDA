# l = [8,9,15]
#
# for e in l:
#     print(e)

###############################################

# l = [7,9,10,12]
# p = int(input("Digite um número a pequisar:"))
#
# for e in l:
#     if e == p:
#         print("Elemento encontrado!")
#         break
# else:
#     print("Elemento não encontrado!")

###############################################

# for v in range(3,33,3):
#     print(v, end=" Achou")
#     print()

###############################################

# l = list(range(100,1100,50))
# print(l)

###############################################

#Apresentar o índice e o número do índice

# l = [5,9,13]
# x = 0
#
# for e in l:
#     print("[%d] %d" %(x,e))
#     x += 1

###############################################

# l = [5,9,13]
#
# for x, e in enumerate(l):
#     print("[%d] %d" %(x,e))

###############################################

# l = [1,7,2,4]
# maximo = l[0]
#
# for e in l:
#     if e > maximo:
#         maximo = e
# print(maximo)

###############################################

# !!!!!!!!

# v = [9,8,7,12,0,13,21]
# p = []
# i = []
#
# for e in v:
#     if e % 2 == 0:
#     p.append(e)
# else:
#     i.append(e)
# print("Pares", p)
# print("Impares", i)

###############################################

# lugares_vagos = [10,2,1,3,0]
#
# while True:
#     sala = int(input("Estacionamento (0 sai):"))
#     if sala == 0:
#         print("Fim")
#         break
#     if sala > len(lugares_vagos) or sala < 1:
#         print("Estacionamento inválido")
#     elif lugares_vagos[sala - 1] == 0:
#         print("Desculpe, estacionamento lotado!")
#     else:
#         lugares = int(input("Quantos lugares você deseja (%d vagas):"
#         % lugares_vagos[sala-1]))
#         if lugares > lugares_vagos[sala-1]:
#             print("Esse número de lugares não está disponível.")
#         elif lugares < 0:
#             print("Número inválido")
#         else:
#             lugares_vagos[sala-1] -= lugares
#             print("%d lugares ocupados" % lugares)
# print("Utilização dos Estacionamento")
#
# for x,l in enumerate(lugares_vagos):
#     print("Sala %d - %d lugar(es) vazio(s)" % (x + 1, l))

###############################################

# s = ["maçãs", "peras", "kiwis"]
# print(len(s))
# s.append("uvas")
# print(s[3])

###############################################

# compras = []
#
# while True:
#     produto = input("Produto:")
#     if produto == "Fim" or "fim":
#         break
#     compras.append(produto)
# for h in compras:
#     print(h)

###############################################

# s = ["maçãs", "peras", "kiwis"]
#
# print(s[1][2])

###############################################

# l = ["maçãs", "peras", "kiwis"]
#
# for s in l:
#     for letra in s:
#         print(letra)

###############################################

# produto1 = ["maçã", 10, 0.30]
# produto2 = ["pera", 5, 0.75]
# produto3 = ["kiwi", 4, 0.98]
# compras = [produto1, produto2, produto3]
#
# for e in compras:
#     print("Produto: %s" % e[0])
#     print("Quantidade: %d" % e[1])
#     print("Preço: %5.2f" % e[2])

###############################################

# compras = []
#
# while True:
#     produto = input("Produto:")
#     if produto == "fim":
#         break
#     quantidade = int(input("Quantidade:"))
#     preco = float(input("Preço:"))
#     compras.append([produto, quantidade, preco])
#     soma = 0.0
# for e in compras:
#     print("%20s %5d %5.2f %6.2f" % (e[0], e[1], e[2], e[1] * e[2]))
#     soma += e[1] * e[2]
# print("Total: %7.2f" % soma)

###############################################

# lista1 = []
# lista2 = []
#
# while True:
#     x = int(input("Digite um número para a lista 1 (0 sai):"))
#     if x == 0:
#         break
#     lista1.append(x)
# while True:
#     x = int(input("Digite u número para a lista 2 (0 sai):"))
#     if x == 0:
#         break
#     lista2.append(x)
# lista3 = lista1[:]
# lista3.extend(lista2)
# y = 0
# while y < len(lista3):
#     print(f"{y}: {lista3[y]}")
#     x = x + 1

# import numpy as np
#
# notas = []
#
# while True:
#     x = float(input("Digite apenas oito notas (0 sai): "))
#     if x == 0:
#         break
#     notas.append(x)
#
# media = np.mean(notas)
#
# print("Sua média foi de", media)



