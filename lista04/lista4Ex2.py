import pandas as pd
import matplotlib.pyplot as plot
import numpy as np

# Exercicio 2

pessoas = {"N. Erros": [6,8,6,10,8,14,12,14,12,16],
           "Horas sem errar": [8,8,12,12,16,16,20,20,24,24]}

matriz_corr = pessoas["N. Erros"], pessoas["Horas sem errar"]
rho = np.corrcoef(matriz_corr)
print('Resultado da correlação Linar:')
print(rho)

'''
    Conforme a apresentação da matriz de correlação,
podemos chegar a uma conclusão de uma alta correlação de 0.80, entre
os números de erros e as horas sem errar.

'''