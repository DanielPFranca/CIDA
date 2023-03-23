# Carregamentos das bibliotecas
import pandas as pd
import matplotlib.pyplot as plot
import numpy as np

# Carregamento dos dados a partir do .csv
arquivo = "dados_seguros.csv"
dados = pd.read_csv(arquivo, header=1) # Faz a leitura do cvs e informa a linha do cabeçalho

dados_dict = dados.to_dict("list") # Converte o dataframe para um dicionário
print(dados_dict)

# Processamento dos dados


q1 = np.percentile(dados_dict['Fatia de Mercado'], 25, method="averaged_inverted_cdf")
q3 = np.percentile(dados_dict['Fatia de Mercado'], 75, method="averaged_inverted_cdf")

dq = q3 - q1

lim_inf = np.fmax(min(dados_dict['Fatia de Mercado']), q1 - 1.5*dq)
lim_sup = np.fmin(max(dados_dict['Fatia de Mercado']), q3 + 1.5*dq)

# Determina o tamanho dos dados

tamanho = len(dados_dict["Fatia de Mercado"])
contador = range(tamanho) # cria uma sequencia de contagem
# Identifica os outliers
for i in contador:
    if ((dados_dict["Fatia de Mercado"][i] > lim_sup ) or (dados_dict["Fatia de Mercado"][i] < lim_inf)):
        print("Outlier: ", dados_dict["Ramo"][i]), " - ", dados_dict["Fatia de Mercado"][i]


# Apresentação dos dados

print(dados_dict)
print("Limite Inferior:", lim_inf)
print("Limite Superior:", lim_sup)

diagrama = plot.boxplot(dados_dict['Fatia de Mercado'])
plot.show()