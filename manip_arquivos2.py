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

pop_sudeste = list(zip())

for i in contador:
    if ((dados_dict["Estado"][i]) in (["SP", "MG", "ES", "RJ"])):
        pop_sudeste.append(dados_dict["População"][i],)

print(pop_sudeste)

print("Limite Inferior:", lim_inf)
print("Limite Superior:", lim_sup)

diagrama = plot.boxplot(dados_dict["População"], positions= [1])
diagrama2 = plot.boxplot(pop_sudeste, positions= [2])
#plot.show()

tamanho = len(dados_dict["Estado"])
contador = range(tamanho)

pop_nordeste = []
cidades_nordeste = []
estados_nordeste = ["MA", "PI", "CE", "RN", "PB", "PE", "AL", "SE", "BA"]
tupla_nordeste = list(zip()) # Cria uma lista de tuplas vazia
# Supondo que os dados não são fornecidos de forma ordenada, vamos precisar ordenar as cidades por população
# Tupla: Conjunto de dados agrupados
################################################################
for i in contador: # Percorre todas as cidades do arquivo
    if (dados_dict["Estado"][i] in estados_nordeste):
        #t = (dados_dict["Município"][i], dados_dict["População"][i])
        t = (dados_dict["População"][i], dados_dict["Município"][i]) # Invertida, para o sort não ordenar pelas cidades, e sim pela população
        tupla_nordeste.append(t)
tupla_nordeste.sort()
#print(tupla_nordeste)
        #pop_nordeste.append(dados_dict["População"][i])
        #cidades_nordeste.append(dados_dict["Município"][i])

# Impressão das 3 cidades menos populosas
print("Cidades menos populosas do nordeste: ")
print(tupla_nordeste[0], tupla_nordeste[1], tupla_nordeste[2])

# OU ->>>

# for i in contador:
#     if ((dados_dict["Estado"][i]) in (["MA", "PI", "CE", "RN", "PB", "PE", "AL", "SE", "BA"])):
#         pop_nordeste.append(dados_dict["População"][i])
#         cidades_nordeste.append(dados_dict["Município"][i])
################################################################

# print(pop_nordeste)
# print(cidades_nordeste)
