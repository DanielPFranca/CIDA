
import pandas as pd
import matplotlib.pyplot as plot
import numpy as np
# Lista 4
# Exercicio 3


alimento = {"Unidades": [40,60,80,100,120,140,160],
            "Rendimento": [15.9, 18.8, 21.6, 25.2, 28.7, 30.4, 30.7]
            }

dispersao = plt.scatter(alimento["Unidades"], alimento["Rendimento"])
plt.show()

matriz_corr = alimento["Unidades"], alimento["Rendimento"]
rho = np.corrcoef(matriz_corr)
print('Resultado da correlação Linar:')
print(rho)