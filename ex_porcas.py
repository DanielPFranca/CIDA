
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



arquivo = "dados_porcas"
dados = pd.read_csv(arquivo, header=0)
dados_dict = dados.to_dict("list")


tamanho = len(dados_dict["d"])
contador = range(tamanho)

r =[]
k = []
for i in contador:
    valor=dados_dict["d"][i] / dados_dict["h"][i]
    r.append(valor)

    valor = dados_dict["d"][i] * dados_dict["h"][i]
    k.append(valor)

# Verificar as correlações de Pearson (Linear)

matriz_corr = [dados_dict["Porca"], dados_dict["h"], dados_dict["d"], dados_dict["m"], r, k]
rho = np.corrcoef(matriz_corr)
print('Resultado da correlação Linar:')
print(rho, "\n")


tamanho = len(dados_dict["m"])
contador = range(tamanho)
porca_log = []
altura_log = []
diametro_log = []
r_log = []
k_log = []
massa_log = []

for i in contador:
    valor = np.log(dados_dict["Porca"][i])
    porca_log.append(valor)

    valor = np.log(dados_dict["h"][i])
    altura_log.append(valor)

    valor = np.log(dados_dict["d"][i])
    diametro_log.append(valor)

    valor = np.log(r[i])
    r_log.append(valor)

    valor = np.log(k[i])
    k_log.append(valor)

    valor = np.log(dados_dict["m"][i])
    massa_log.append(valor)

# Verificar as correlações de Pearson (não Linear)

matriz_correlacao_n_linear = [porca_log, altura_log, diametro_log, massa_log, k_log]
rho_linearizado = np.corrcoef(matriz_correlacao_n_linear)

print('Resutado da correlação não-Linear')
print(rho_linearizado)


# graf1 = plt.scatter(dados_dict["Porca"], dados_dict["m"])
# plt.title('Massa em função do tipod de porca')
# plt.xlabel('Porca')
# plt.ylabel('Massa')
#plt.show()

# graf2 = plt.scatter(dados_dict["h"], dados_dict["m"])
# plt.title('Massa em função da altura')
# plt.xlabel('Altura da porca')                           #Não Linear
# plt.ylabel('Massa')
# plt.show()

# graf3 = plt.scatter(dados_dict["d"], dados_dict["m"])
# plt.title('Massa em função do diâmetro')
# plt.xlabel('Diâmetro da porca')                         #Não Linear
# plt.ylabel('Massa')
# plt.show()
#
#
# graf4 = plt.scatter(k, dados_dict["m"])
# plt.title('Massa um função da razãoK')
# plt.xlabel('Razão-K')                                   #Não Linear
# plt.ylabel('Massa')
# plt.show()

# Diâmetro em função da altura
# graf5 = plt.scatter(dados_dict["d"], dados_dict["h"])
# plt.show()


# Diâmetro em função do tipo de porca
graf6 = plt.scatter(dados_dict["Porca"], dados_dict["d"])
plt.show()


# Altura em função da altura
# graf7 = plt.scatter(dados_dict["Porca"], dados_dict["h"])
# plt.show()

# graf6 = plt.scatter(dados_dict["Porca"], dados_dict["m"])
# plt.show()