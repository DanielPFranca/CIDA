import numpy as np
import statistics as st
import matplotlib.pyplot as plt

##############################################################################################
#
# # Exercicio 2 da lista
#
# # lesoes = {"Basquete": [1, 4, 4, 7, 3, 3, 2, 4, 5, 2, 4, 3, 5, 3, 2, 4, 3, 6, 5],
# #           "Futebol": [1, 7, 7, 6, 1, 2, 6, 1, 2, 6, 1, 7, 2, 1, 3, 2, 7, 5, 6, 1, 7, 4, 1, 5, 7, 6, 3, 2]}
# #
# # media = np.mean(lesoes["Basquete"])
# # media2 = np.mean(lesoes["Futebol"])
# #
# # mediana = np.median(lesoes["Basquete"])
# # mediana2 = np.median(lesoes["Futebol"])
# #
# # desvio_padrao = np.std(lesoes["Basquete"])
# # desvio_padrao2 = np.std(lesoes["Futebol"])
# #
# #
# # print("A média de lesões no basquete é de: %.2f" %media)
# # print("A média de lesões no futebol é de: %.2f" %media2)
# #
# # print("A mediana de lesões no basquete é de: %.2f" %mediana)
# # print("A mediana de lesões no futebol é de: %.2f" %mediana2)
# #
# # print("O desvio padrão de lesões no basquete é de: %.2f" %desvio_padrao)
# # print("O desvio padrão de lesões no futebol é de: %.2f" %desvio_padrao2)
# #
# # valores = lesoes["Basquete"]
# # valores2 = lesoes["Futebol"]
# #
# # Q1 = np.percentile(valores, 25, method="averaged_inverted_cdf")
# # Q3 = np.percentile(valores, 75, method="averaged_inverted_cdf")
# #
# # # dureza.sort()
# # # print(dureza)
# #
# # DQ = Q3 - Q1
# #
# # Limite_inferior = np.fmax(min(valores), Q1-1.5*DQ)
# # Limite_superior = np.fmin(max(valores), Q3+1.5*DQ)
# #
# # print("Limite superior = %.2f" % (Limite_superior))
# # print("Limite inferior = %.2f" % (Limite_inferior))
# #
# # print("O futebol é mais propício à ter um número maior de lesões em relação ao basquete")
# #
# # diagrana = plt.boxplot(valores, positions=[1])
# # diagrana = plt.boxplot(valores2, positions=[2])
# # plt.show()
# #
# # print("O futebol é mais propício à ter mais lesões")
#
# ##############################################################################################
#
# # Exercicio 3 da lista
# # Questão A)
# notas = {"Alunas": [154, 109, 137, 115, 152, 140, 154, 178, 101, 103, 126, 126, 137, 165, 165,  129, 200, 148],
#          "Alunos": [108, 140, 114, 91, 180, 115, 126, 92, 169, 146, 109, 132, 75, 88, 113, 151, 70, 115, 187, 104]}
#
# media = np.mean(notas["Alunas"])
# media2 = np.mean(notas["Alunos"])
#
# mediana = np.median(notas["Alunas"])
# mediana2 = np.median(notas["Alunos"])
#
# print("A média das alunas é de: %.2f" %media)
# print("A média dos alunos é de: %.2f" %media2)
#
# print("A mediana das alunas é de: %.2f" %mediana)
# print("A mediana dos alunos é de: %.2f" %mediana2)
#
#
# ###############################################################################################################
# #Questão B)
#
# valores = notas["Alunas"]
# valores2 = notas["Alunos"]
#
# Q1 = np.percentile(valores, 25, method="averaged_inverted_cdf")
# Q3 = np.percentile(valores, 75, method="averaged_inverted_cdf")
#
# # dureza.sort()
# # print(dureza)
#
# DQ = Q3 - Q1
#
# Limite_inferior = np.fmax(min(valores), Q1-1.5*DQ)
# Limite_superior = np.fmin(max(valores), Q3+1.5*DQ)
#
# print("Limite superior = %.2f" % (Limite_superior))
# print("Limite inferior = %.2f" % (Limite_inferior))
#
#
# # diagrama = plt.boxplot(valores, positions=[1])
# # diagrama2 = plt.boxplot(valores2, positions=[2])
# # plt.show()
#
#
# notas_limpas = []
# for indices in range(len(notas["Alunas"])):
#     if (notas["Alunas"][indices] > Limite_inferior) and (notas["Alunas"][indices] < Limite_superior):
#         notas_limpas.append(notas["Alunas"][indices])
#
# # diagrama = plt.boxplot(valores, positions=[1])
# # diagrama2 = plt.boxplot(notas_limpas, positions=[2])
#
# mediasecundaria = np.mean(notas_limpas)
# media2_1 = np.mean(notas["Alunos"])
# print("Resultado da média recalculada: %.2f" %mediasecundaria)
# print("Média dos alunos novamente: %.2f" %media2_1)
#
# medianasecundaria = np.median(notas_limpas)
# mediana2_1 = np.median(notas["Alunos"])
#
# print("Resultado da mediana recalculada: %.2f" %medianasecundaria)
# print("Mediana dos alunos novamente: %.2f" %mediana2_1)
#
# ###############################################################################################################
# #Questão C)
#
# notasturma = notas["Alunas"] + notas["Alunos"]
# #print(notasturma)
#
# diagrama = plt.boxplot(valores, positions=[1])
# diagrama2 = plt.boxplot(valores2, positions=[2])
# diagrama3 = plt.boxplot(notasturma, positions=[3])
#
# print("Após a construção dos boxplots, chegamos a uma conclusão de que o desempenho do grupo de alunos é maior que o das alunas")
#
# #plt.show()
#
# ##############################################################################################
#
# #Exercicio 4 da lista
# #Questão A)
#
# funcionarios = {"Salário": [13876, 11608, 18701, 11283, 11767, 20872, 11772, 10535, 12195, 12313, 14975, 21371, 19800, 11417,
#                             20263, 13231, 12884, 13245, 15956, 12336, 21352, 13839, 16978, 14803, 22184, 13548, 14467, 15942, 23174, 23780],
#                 "Experiência(anos)": [1, 1, 1, 1, 1, 2, 2, 2, 2,3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 6, 6, 6, 7, 8, 8, 8, 10, 10, 10, 10],
#                 "Educação": ["Bacharel", "Doutorado", "Doutorado", "Mestrado", "Doutorado", "Mestrado", "Mestrado", "Bacharel", "Doutorado", "Mestrado",
#                          "Bacharel", "Mestrado", "Doutorado", "Bacharel", "Doutorado", "Doutorado", "Mestrado", "Mestrado", "Bacharel", "Bacharel",
#                          "Doutorado", "Mestrado", "Bacharel", "Mestrado", "Doutorado", "Bacharel", "Bacharel", "Mestrado", "Doutorado", "Mestrado"],
#                 "Gestão": ["Sim", "Não", "Sim", "Não", "Não", "Sim", "Não", "Não", "Não", "Não", "Sim", "Sim", "Sim", "Não", "Sim", "Não", "Não", "Não",
#                            "Sim", "Não", "Sim", "Não", "Sim", "Não", "Sim", "Não", "Não", "Não", "Sim", "Sim"]
#                 }
#
#
#
#
# print(funcionarios["Salário"], ["Educação"])

##############################################################################################

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
print("Médias calculadas: %.2f" %media_1)
print("Médias calculadas: %.2f" %media_2)
print("Médias calculadas: %.2f" %media_3)


mediana_1 = np.median(disciplinas["Direito"])
mediana_2 = np.median(disciplinas["Política"])
mediana_3 = np.median(disciplinas["Estatística"])
print("Mediana calculada: %.2f" %mediana_1)
print("Mediana calculada: %.2f" %mediana_2)
print("Mediana calculada: %.2f" %mediana_3)

desvio_padrao_1 = np.std(disciplinas["Direito"])
desvio_padrao_2 = np.std(disciplinas["Política"])
desvio_padrao_3 = np.std(disciplinas["Estatística"])
print("DP calculado: %.2f" %desvio_padrao_1)
print("DP calculado: %.2f" %desvio_padrao_2)
print("DP calculado: %.2f" %desvio_padrao_3)

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


diagrama_1 = plt.boxplot(a1, positions=[1])
diagrama_2 = plt.boxplot(a2, positions=[2])
diagrama_3 = plt.boxplot(a3, positions=[3])
plt.show()


