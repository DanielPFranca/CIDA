import numpy as np
import statistics as st
import matplotlib.pyplot as plt

##############################################################################################

# Exercicio 2 da lista

#A)

lesoes = {"Basquete": [1, 4, 4, 7, 3, 3, 2, 4, 5, 2, 4, 3, 5, 3, 2, 4, 3, 6, 5],
          "Futebol": [1, 7, 7, 6, 1, 2, 6, 1, 2, 6, 1, 7, 2, 1, 3, 2, 7, 5, 6, 1, 7, 4, 1, 5, 7, 6, 3, 2]}

media = np.mean(lesoes["Basquete"])
media2 = np.mean(lesoes["Futebol"])

mediana = np.median(lesoes["Basquete"])
mediana2 = np.median(lesoes["Futebol"])

desvio_padrao = np.std(lesoes["Basquete"])
desvio_padrao2 = np.std(lesoes["Futebol"])


print("A média de lesões no basquete é de: %.2f" %media)
print("A média de lesões no futebol é de: %.2f" %media2)

print("A mediana de lesões no basquete é de: %.2f" %mediana)
print("A mediana de lesões no futebol é de: %.2f" %mediana2)

print("O desvio padrão de lesões no basquete é de: %.2f" %desvio_padrao)
print("O desvio padrão de lesões no futebol é de: %.2f" %desvio_padrao2)


#B)


valores = lesoes["Basquete"]
valores2 = lesoes["Futebol"]

Q1 = np.percentile(valores, 25, method="averaged_inverted_cdf")
Q3 = np.percentile(valores, 75, method="averaged_inverted_cdf")

# dureza.sort()
# print(dureza)

DQ = Q3 - Q1

Limite_inferior = np.fmax(min(valores), Q1-1.5*DQ)
Limite_superior = np.fmin(max(valores), Q3+1.5*DQ)

print("Limite superior = %.2f" % (Limite_superior))
print("Limite inferior = %.2f" % (Limite_inferior))

print("O futebol é mais propício à ter um número maior de lesões em relação ao basquete")

diagrana = plt.boxplot(valores, positions=[1])
diagrana = plt.boxplot(valores2, positions=[2])
plt.show()

print("O futebol é mais propício à ter mais lesões")