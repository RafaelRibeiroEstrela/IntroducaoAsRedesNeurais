

import tensorflow as tf
import abrirTxt
import numpy as np


def fu (x1, x2, w1, w2):

	u = x1 * w1 + x2 * w2

	return sigmoid (u)


def fy (y1, w3):

	u = y1 * w3

	return sigmoid (u)


def sigmoid (x):

	return 1 / 1 + np.exp (x)


entrada_global = abrirTxt.txt ()

x1 = entrada_global
del (x1[-1])
x2 = entrada_global [1:]
w1 = w2 = w3 = 0
saida_esperada = entrada_global [2:]
fator_aprendizado = 0.02

for i in range (len(saida_esperada)):

	y1 = fu (x1[i], x2[i], w1, w2)

	y2 = fy (y1, w3)

	erro = saida_esperada[i] - y2

	if (erro != 0):

		while (True):

			w3 = w3 + fator_aprendizado * erro * y1
			w2 = w2 + fator_aprendizado * erro * x2[i]
			w1 = w1 + fator_aprendizado * erro * x1[i]

			print ('w1, w2, w3:', w1, w2, w3)


			y1 = fu (x1[i], x2[i], w1, w2)
			y2 = fy (y1, w3)

			erro = saida_esperada[i] - y2

			print ('erro:', erro)

			if (erro == 0):

				break

print (w1, w2, w3)



