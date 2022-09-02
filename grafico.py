# Usando o módulo Time (Built-in) e Matplotlib(Externo), faça um programa que pede que o usuário digite uma palavra
# 5 vezes seguidas. Conte o tempo que ele leva para digita a palavra a cada repetição e ao final gere um gráfico com os
# tempos.

import matplotlib.pyplot as plt
import time as t

tempos = []
vezes = []
vez = 1

print('Este programa marcará o tempo gasto para digitar qualquer palavra. Você terá que digitá-la 5 vezes')

input('Aperte enter para começar.')
print('\n')

while vez <= 5:
        inicio = t.perf_counter()
        input('Digite a palavra: ')
        fim = t.perf_counter()
        tempo = round(fim - inicio, 1)
        tempos.append(tempo)
        vezes.append(vez)
        vez += 1

legenda = ['1 vez', '2 vez', '3 vez', '4 vez', '5 vez']
plt.xticks(vezes, legenda)
plt.plot(vezes, tempos)
plt.show()


