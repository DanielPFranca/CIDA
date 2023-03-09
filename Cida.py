import numpy as np
import statistics as st
import matplotlib.pyplot as plt


dados = [45, 56, -89.0, 23.4, 1.5, 2.5, 5.5, 10.0, -50.0, 1.0]

dados.append(-12.5)
print(dados)

Q1 = np.percentile(dados, 25, method="averaged_inverted_cdf")

Q3 = np.percentile(dados, 75, method="averaged_inverted_cdf")

DQ = Q3 - Q1

Limite_inferior = np.fmax(min(dados), Q1-1.5*DQ)
Limite_superior = np.fmin(max(dados), Q3+1.5*DQ)

#Eliminar outliers
dados_limpos = []
for indices in range(len(dados)):
    if (dados[indices] > Limite_inferior) and (dados[indices] < Limite_superior):
        dados_limpos.append(dados[indices])


diagrana = plt.boxplot(dados, positions=[1])
diagrama2 = plt.boxplot(dados_limpos, positions=[2])
print(dados_limpos)
plt.show()
