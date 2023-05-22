import numpy as np
import statistics as st
import matplotlib.pyplot as plt

# Exercicio 1 lista - Estruturas de Dados

dados = [53.0, 70.2, 84.3, 69.5, 77.8, 87.5,53.4, 82.5, 67.3,
         54.1, 70.5, 71.4, 95.4, 51.1, 74.4, 55.7, 63.5, 85.8,
         53.5, 64.3, 82.7, 78.5, 55.7, 69.1, 72.3, 59.5, 55.3,
         73.0,52.4, 50.7]


#A)

q1 = np.percentile(dados, 25, method="averaged_inverted_cdf")
q2 = np.percentile(dados, 50, method="averaged_inverted_cdf")
q3 = np.percentile(dados, 75, method="averaged_inverted_cdf")

dq = q3 - q1

#Limites do boxplot
Limite_Inferior = np.fmax(min(dados), q1 - 1.5 * dq)
Limite_Superior = np.fmin(max(dados), q3 + 1.5 * dq)

diagrama = plt.boxplot(dados)
plt.show()

'''
    O boxplot não apresentou nenhum Outlier
'''

#B)

qtd_dados = len(dados)
k = 1 + 3.32 * np.log10(qtd_dados)
k = np.round(k)

qtd, classes = np.histogram(dados, bins=int(k))
print(qtd_dados)
print(qtd)
print(classes)
print(k)

'''
    Ao realizar a conta cheguei no resultado de 114,63,
porém acredito que não esteja certo.
'''

#C)

'''
    Feita a tabela de distribuição, a faixa de valores, onde se encontra 80% 
dos valores de dureza seria de 80.5 à 87.95 
'''

#D)

dados2 = [53.0, 70.2, 84.3, 69.5, 77.8, 87.5,53.4, 82.5, 67.3,
         54.1, 70.5, 71.4, 95.4, 51.1, 74.4, 55.7, 63.5, 85.8,
         53.5, 64.3, 82.7, 78.5, 55.7, 69.1, 72.3, 59.5, 55.3,
         73.0,52.4, 50.7]

Q1 = np.percentile(dados2, 25, method="averaged_inverted_cdf")
Q2 = np.percentile(dados2, 50, method="averaged_inverted_cdf")
Q3 = np.percentile(dados2, 75, method="averaged_inverted_cdf")

DQ = Q3 - Q1

Limite_Inferior2 = np.fmax(min(dados), Q1 - 2.5 * DQ)
Limite_Superior2 = np.fmin(max(dados), Q3 + 2.5 * DQ)

diagrama2 = plt.boxplot(dados2)
plt.show()
