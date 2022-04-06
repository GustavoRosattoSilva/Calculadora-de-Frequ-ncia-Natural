import numpy
import pandas
import seaborn

picos = []

auxiliar = []

data = []

df = pandas.read_table('x.dat' , sep = ' ', names = ['Temp','Angulo'])
	
data = df.values

def encontrar_picos():

	for x in range(len(data)):

		if (x == 0):

			auxiliar.append(data[x])

		if ((x - 1 >= 0) and(x + 1 < len(data))):

			if ((data[x][1] > data[x - 1][1]) and (data[x][1] > data[x + 1][1])):

				auxiliar.append(data[x])

	for x in range(len(auxiliar)):

		k = []

		if(x + 1 < len(auxiliar)):

			if (auxiliar[x][1] > auxiliar[x-1][1]):

				k.append(auxiliar[x][0])

				k.append(auxiliar[x][1])

				picos.append(k)
	
def periodo():

	T = 0

	for x in range(len(picos)):


		if (x > 0):

			T += (picos[x][0] - picos[x - 1][0])

	T = T / (len(picos) - 1)

	return T

def velocidade_angular():

	return 2*numpy.pi/periodo()

def sigma():

	x = 0 

	s = 0

	while ((picos[0][1]/2) < (picos[x + 1][1])):

		s += numpy.log((picos[x][1]/picos[x+1][1]))

		x +=  1 
	
	return s/x

def csi():

	return  sigma()/numpy.sqrt((1-sigma()**2))

def frequencia_natural():

	encontrar_picos()

	return velocidade_angular()/numpy.sqrt(1 - csi()**2)

print(frequencia_natural())
