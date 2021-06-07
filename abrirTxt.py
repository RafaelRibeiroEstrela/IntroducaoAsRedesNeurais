

import string


def txt():
	
	with open ('leite_integral.txt', 'r') as linha:

		arquivo = linha.read ()

	arquivo = arquivo.translate({ord(c): None for c in string.whitespace})

	lista = []

	for i in range (len(arquivo)):

		lista.append (int (arquivo[i]))

	return lista
