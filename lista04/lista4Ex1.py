import pandas as pd
import matplotlib.pyplot as plot
import numpy as np

# Lista 4 Exercicio 1
# Questão A)

arquivo = "dados_imposto_empresas.csv"
dados = pd.read_csv(arquivo, header=2, sep=";")

dados_dict = dados.to_dict("list")
print(dados_dict["Imposto (%)"])

qtd_dados = len(dados_dict["Imposto (%)"])
k = 1 + 3.32 * np.log10(qtd_dados)
k = np.round(k)

qtd, classes = np.histogram(dados_dict["Imposto (%)"], bins=int(k))

diagrama = plot.hist(dados_dict["Imposto (%)"], bins=int(k))
plot.show()


