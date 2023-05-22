import numpy as np
import statistics as st
import matplotlib.pyplot as plt

# Exercicio 3 da lista
# Questão A)
notas = {"Alunas": [154, 109, 137, 115, 152, 140, 154, 178, 101, 103, 126, 126, 137, 165, 165,  129, 200, 148],
         "Alunos": [108, 140, 114, 91, 180, 115, 126, 92, 169, 146, 109, 132, 75, 88, 113, 151, 70, 115, 187, 104]}

media = np.mean(notas["Alunas"])
media2 = np.mean(notas["Alunos"])

mediana = np.median(notas["Alunas"])
mediana2 = np.median(notas["Alunos"])

print("A média das alunas é de: %.2f" %media)
print("A média dos alunos é de: %.2f" %media2)

print("A mediana das alunas é de: %.2f" %mediana)
print("A mediana dos alunos é de: %.2f" %mediana2)


# Questão B)


valores = notas["Alunas"]
valores2 = notas["Alunos"]

Q1 = np.percentile(valores, 25, method="averaged_inverted_cdf")
Q3 = np.percentile(valores, 75, method="averaged_inverted_cdf")

# dureza.sort()
# print(dureza)

DQ = Q3 - Q1

Limite_inferior = np.fmax(min(valores), Q1-1.5*DQ)
Limite_superior = np.fmin(max(valores), Q3+1.5*DQ)

print("Limite superior = %.2f" % (Limite_superior))
print("Limite inferior = %.2f" % (Limite_inferior))


# diagrama = plt.boxplot(valores, positions=[1])
# diagrama2 = plt.boxplot(valores2, positions=[2])
# plt.show()


notas_limpas = []
for i in range(len(notas["Alunas"])):
    if (notas["Alunas"][i] > Limite_inferior) and (notas["Alunas"][i] < Limite_superior):
        notas_limpas.append(notas["Alunas"][i])

# diagrama = plt.boxplot(valores, positions=[1])
# diagrama2 = plt.boxplot(notas_limpas, positions=[2])

mediasecundaria = np.mean(notas_limpas)
media2_1 = np.mean(notas["Alunos"])
print("Resultado da média recalculada: %.2f" %mediasecundaria)
print("Média dos alunos novamente: %.2f" %media2_1)

medianasecundaria = np.median(notas_limpas)
mediana2_1 = np.median(notas["Alunos"])

print("Resultado da mediana recalculada: %.2f" %medianasecundaria)
print("Mediana dos alunos novamente: %.2f" %mediana2_1)

# Questão C)

notasturma = notas["Alunas"] + notas["Alunos"]
#print(notasturma)

diagrama = plt.boxplot(valores, positions=[1])
diagrama2 = plt.boxplot(valores2, positions=[2])
diagrama3 = plt.boxplot(notasturma, positions=[3])

print("Após a construção dos boxplots, chegamos a uma conclusão de que o desempenho do grupo de alunos é maior que o das alunas")

plt.show()

