import numpy as np
import statistics as st
import matplotlib.pyplot as plt

#Exercicio 4 da lista
#Questão A)

funcionarios = {"Salário": [13876, 11608, 18701, 11283, 11767, 20872, 11772, 10535, 12195, 12313, 14975, 21371, 19800, 11417,
                            20263, 13231, 12884, 13245, 15956, 12336, 21352, 13839, 16978, 14803, 22184, 13548, 14467, 15942, 23174, 23780],
                "Experiência(anos)": [1, 1, 1, 1, 1, 2, 2, 2, 2,3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 6, 6, 6, 7, 8, 8, 8, 10, 10, 10, 10],
                "Educação": ["Bacharel", "Doutorado", "Doutorado", "Mestrado", "Doutorado", "Mestrado", "Mestrado", "Bacharel", "Doutorado", "Mestrado",
                         "Bacharel", "Mestrado", "Doutorado", "Bacharel", "Doutorado", "Doutorado", "Mestrado", "Mestrado", "Bacharel", "Bacharel",
                         "Doutorado", "Mestrado", "Bacharel", "Mestrado", "Doutorado", "Bacharel", "Bacharel", "Mestrado", "Doutorado", "Mestrado"],
                "Gestão": ["Sim", "Não", "Sim", "Não", "Não", "Sim", "Não", "Não", "Não", "Não", "Sim", "Sim", "Sim", "Não", "Sim", "Não", "Não", "Não",
                           "Sim", "Não", "Sim", "Não", "Sim", "Não", "Sim", "Não", "Não", "Não", "Sim", "Sim"]
                }

q1 = np.percentile(funcionarios["Salário"], 25, method="averaged_inverted_cdf")
q2 = np.percentile(funcionarios["Salário"], 50, method="averaged_inverted_cdf")
q3 = np.percentile(funcionarios["Salário"], 75, method="averaged_inverted_cdf")

dq = q3 - q1

# Limites do boxplot
Limite_Inferior = np.fmax(min(funcionarios["Salário"]), q1 - 1.5 * dq)
Limite_Superior = np.fmin(max(funcionarios["Salário"]), q3 + 1.5 * dq)

diagrama = plt.boxplot(funcionarios["Salário"])
plt.show()

'''
    Não entendi a questão
'''