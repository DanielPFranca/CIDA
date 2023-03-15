import numpy as np

lista_dados = [-0.5, 1.8, 43.8, 52, 2.6, 7.8, 9.8, -2.5]

x = lista_dados[3]
y = lista_dados[0 : 2] # Para obter um intervalo entre os dados
print(y)

lista_dados.append(90) # Para adicionar um dado no final da lista
print(lista_dados)

loop = range(len(lista_dados))
print(loop)

dados = {"Material": ["Aluminio", "Aço", "ABS", "Bronze", "FoFo"],
      "Elasticidade": [70.0, 210.0, 2.5, 75.0, 190.0]}

z = dados["Elasticidade"] # Retorna em z toda a lista de números
print(z)

w = dados["Elasticidade"][1]
print("O indice idicado é o :", w)

media = np.mean(z)
print("A média dos dados é:", media)
