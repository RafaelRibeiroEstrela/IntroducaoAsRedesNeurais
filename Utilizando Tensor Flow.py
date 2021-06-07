import tensorflow as tf
		
#Utilizando o tensorflow

print ("\nMODO PRINCIPAL - Utilizando tensorflow\n")
	
x = tf.constant ([0.56,0.29,0.19])
w1 = tf.constant ([0.89,0.5,0.18])
w2 = tf.constant ([0.7,0.19,0.56])
w3 = tf.constant ([0.7,0.18,0.84])

m1 = tf.multiply (x,w1)
m2 = tf.multiply (x,w2)
m3 = tf.multiply (x,w3)

s1 = tf.reduce_sum (m1)
s2 = tf.reduce_sum (m2)
s3 = tf.reduce_sum (m3)

fx = tf.constant (0.3)

y1 = s1 + fx
y2 = s2 + fx
y3 = s3 + fx

print (y1,"\n", y2,"\n", y3)

#Utilizando listas

print ("\nMODO ALTERNATIVO - Utilizando listas\n")

def modo_alternativo ():
	
	x = [0.56,0.29,0.19]
	w1 = [0.89,0.5,0.18]
	w2 = [0.7,0.19,0.56]
	w3 = [0.7,0.18,0.84]

	lista = [0,0,0]

	for i in range (len(x)):
	
		lista[0] = lista[0] + (x[i] * w1[i])
		lista[1] = lista[1] + (x[i] * w2[i])
		lista[2] = lista[2] + (x[i] * w3[i])
		
	for i in range (len(lista)):
	
		lista[i] = lista[i] + 0.3
	
	print (lista)
	

modo_alternativo ()



