import pandas as pd
import matplotlib.pyplot as plot
import numpy as np

arquivo = "dados_pop.csv"
dados = pd.read_csv(arquivo, header=1)

dados_dict = dados.to_dict("list") # Converte o dataframe para um dicionário
print(dados_dict)


q1 = np.percentile(dados_dict["População"], 25, method="averaged_inverted_cdf")
q3 = np.percentile(dados_dict['População'], 75, method="averaged_inverted_cdf")

dq = q3 - q1

lim_inf = np.fmax(min(dados_dict['População']), q1 - 1.5*dq)
lim_sup = np.fmin(max(dados_dict['População']), q3 + 1.5*dq)

tamanho = len(dados_dict["Estado"])
contador = range(tamanho)

pop_sudeste = []

for i in contador:
    if ((dados_dict["Estado"][i]) in (["SP", "MG", "ES", "RJ"])):
        pop_sudeste.append(dados_dict["População"][i])

print(pop_sudeste)

print("Limite Inferior:", lim_inf)
print("Limite Superior:", lim_sup)

diagrama = plot.boxplot(dados_dict["População"], positions= [1])
diagrama2 = plot.boxplot(pop_sudeste, positions= [2])
#plot.show()

tamanho2 = len(dados_dict["Estado"])
contador2 = range(tamanho2)

pop_nordeste = []
municipio = []

for i in contador:
    if ((dados_dict["Estado"][i]) in (["MA", "PI", "CE", "RM", "PA", "PE", "AL", "SE", "PB"])):
        pop_nordeste.append(dados_dict["População"][i])
        municipio.append(dados_dict["Município"][i])

print(pop_nordeste)
print(municipio)




