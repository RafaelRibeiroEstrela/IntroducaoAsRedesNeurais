
#rede perceptron simples - porta AND

fator_aprendizado = 0.02 #"escolher um valor. menor é melhor"
w1 = 0
w2 = 0
bias = 1

'''
porta and
x1 = [0, 0, 1, 1]
x2 = [0, 1, 0 ,1]
saida_esperada = [0, 0, 0, 1]
'''

'''
porta or
x1 = [0, 0, 1, 1]
x2 = [0, 1, 0 ,1]
saida_esperada = [0, 1, 1, 1]
'''



def mul():
	saida = (x1[i] * w1) + (x2[i] * w2) + bias


se saida < 0 -> fx = 0
se saida >= 0 -> fx = 1

se fx = saida_esperada[i] entao OKK

senão fazer ajuste de peso

erro = saida_esperada - saida
w1_novo = w1 + fator_aprendizado * erro * x1
w2_novo = w2 + fator_aprendizado * erro * x2
b_novo = b + fator_aprendizado * erro

