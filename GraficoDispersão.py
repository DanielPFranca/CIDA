# Carregamento das bibliotecas

import numpy as np
import matplotlib.pyplot as plt

# Entrada dos dados
dados = {"Peso": [30,32,24,28,26,34,25,23,35,31],
         "Altura": [145,150,125,140,127,145,132,112,155,145]}
# Processamento dos dados
# Calculo da correlação de Pearson
peso_medio = np.mean(dados["Peso"])
altura_media = np.mean(dados["Altura"])


# Apresentação dos resultados
print(dados)
print("Peso médio: %5.2f" % peso_medio)
print("Altura média: %5.2f" % altura_media)
dispersao = plt.scatter(dados["Peso"], dados["Altura"], s=100, c = "#4e7179", marker="4")
plt.xlabel("Peso (kg)")
plt.ylabel("Altura (cm)")
#plt.show()
