import numpy as np
import statistics as st
import matplotlib.pyplot as plt

# Exercicio 5 da lista
# Questão A)


disciplinas = {"Seção": ["Pessoal", "Pessoal", "Pessoal", "Pessoal", "Pessoal", "Pessoal", "Pessoal", "Técnica",
                         "Técnica", "Técnica", "Técnica", "Técnica", "Técnica", "Técnica", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas"
                         "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas"],
               "Direito": [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
               "Política": [9.0, 6.5, 9.0, 6.0, 6.5, 6.5, 9.0, 6.0, 9.0, 9.0, 7.0, 5.5, 6.0, 8.0, 7.0, 9.0, 10.0, 5.5, 7.0, 6.0, 6.5, 6.0, 9.0, 6.5, 7.0],
               "Estatística": [9, 9, 8, 8, 9, 10, 8, 8, 9, 8, 10, 7, 7, 9, 8, 7, 8, 9, 2, 7, 7, 8, 9, 8, 7]

            }

media_1 = np.mean(disciplinas["Direito"])
media_2 = np.mean(disciplinas["Política"])
media_3 = np.mean(disciplinas["Estatística"])
print("Médias Direito: %.2f" %media_1)
print("Médias Política: %.2f" %media_2)
print("Médias Estatística: %.2f" %media_3)


mediana_1 = np.median(disciplinas["Direito"])
mediana_2 = np.median(disciplinas["Política"])
mediana_3 = np.median(disciplinas["Estatística"])
print("Mediana Direito: %.2f" %mediana_1)
print("Mediana Política: %.2f" %mediana_2)
print("Mediana Estatística: %.2f" %mediana_3)

desvio_padrao_1 = np.std(disciplinas["Direito"])
desvio_padrao_2 = np.std(disciplinas["Política"])
desvio_padrao_3 = np.std(disciplinas["Estatística"])
print("DP Direito: %.2f" %desvio_padrao_1)
print("DP Política: %.2f" %desvio_padrao_2)
print("DP Estatística: %.2f" %desvio_padrao_3)

#########################################################
# Questão B)

a1 = disciplinas["Direito"]
a2 = disciplinas["Política"]
a3 = disciplinas["Estatística"]

Q1 = np.percentile(a1, 25, method="averaged_inverted_cdf")
Q3 = np.percentile(a1, 75, method="averaged_inverted_cdf")

DQ = Q3 - Q1

Limite_inferior = np.fmax(min(a1), Q1-1.5*DQ)
Limite_superior = np.fmin(max(a1), Q3+1.5*DQ)

print("Limite superior = %.2f" % (Limite_superior))
print("Limite inferior = %.2f" % (Limite_inferior))


# diagrama_1 = plt.boxplot(a1, positions=[1])
# diagrama_2 = plt.boxplot(a2, positions=[2])
# diagrama_3 = plt.boxplot(a3, positions=[3])
# plt.show()
#

# Questão C)

media3coluna = [9, 8.16, 8.7, 7.7, 8.16, 8.5, 8.6, 7.6, 9, 8.6, 8.6, 7.16, 7.3, 8.6, 8,
         8.3, 9, 7.8, 6, 7.3, 7.5, 7.6, 9, 7.8, 7.6]

Q1 = np.percentile(media3coluna, 25, method="averaged_inverted_cdf")
Q3 = np.percentile(media3coluna, 75, method="averaged_inverted_cdf")

DQ = Q3 - Q1

Limite_inferior = np.fmax(min(media3coluna), Q1-1.5*DQ)
Limite_superior = np.fmin(max(media3coluna), Q3+1.5*DQ)

diagrama = plt.boxplot(media3coluna)
#plt.show()

# Questão D)


