import pandas as pd
import matplotlib.pyplot as plot
import numpy as np

# Lista 4
# Exercicio 4
# Questão A)

industria = {"Temperatura": [21.2, 20.3, 22.7, 22, 22.3,23.5,24.8,24.2,25.5,25.2,25.5,25.8,
                             27.5, 26.3, 28.2, 28.6, 29, 29.7, 30.7, 30.3, 30.2, 31.4, 32.5, 32.7],
             "Produtividade": [142,148,131,132,145,138,144,136,141,124, 133,128,
                               132,137,124,117,122,131,124,111,119,129,123,116]
             }

dispersao = plt.scatter(industria["Temperatura"], industria["Produtividade"])
plt.show()

# Questão B)

matriz_corr = industria["Temperatura"], industria["Produtividade"]
rho = np.corrcoef(matriz_corr)
print('Resultado da correlação Linar:')
print(rho)

'''
    Conforme a apresentação da matriz de correlação,
podemos chegar a uma conclusão de uma alta e moderada correlação de -0.77, entre
a temperatura e a produtividade.

'''