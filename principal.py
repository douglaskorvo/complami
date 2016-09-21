import modteste as m
import numpy

n = input('entre com um numero: ')
print "************************************************"
print "************************************************"
print "MOSTRANDO RESULTADO DO CALCULO FEITO PELO MODULO"
print "************************************************"
print "************************************************"
print "numero elevado ao quadrado = %d" %m.pow2(n)
print "numero elevado ao cubo = %d" %m.pow3(n)

import sys
print "***************************"
print "***************************"
print "MOSTRANDO PASTAS DO SISTEMA"
print "***************************"
print "***************************"
for pasta in sys.path:
        print pasta

help(m)

print "***************************"
print "***************************"
print "ABRINDO ARQUIVOS - TIPO 1"
print "***************************"
print "***************************"
file=open("arq.dat","r")
i=0
linha=file.readline()
while(linha):
        print "Linha " +str(i+1)+": "+linha
        linha=file.readline()
        i=+i
file.close()

def abrir(nome):
        print "***************************"
        print "***************************"
        print "ABRINDO ARQUIVOS - TIPO 2"
        print "***************************"
        print "***************************"
        file=open(nome,"r")
        b = str(linha)
        for b in file:
                print b.split()
        file.close()        


print "***************************"
print "***************************"
print "ABRINDO ARQUIVOS - TIPO 3"
print "LEITURA E GRAVACAO"
print "***************************"
print "***************************"
file=open("arq.dat","r")
vetorx=[]
vetory=[]
vetorz=[]
linha=file.readline()
while (linha):
        if (len(linha.split())>2):
                vetorx.append(float(linha.split()[0]))
                vetory.append(float(linha.split()[1]))
                vetorz.append(float(linha.split()[2]))
        linha=file.readline()


vetorxnp=numpy.array(vetorx)
vetorynp=numpy.array(vetory)
vetorznp=numpy.array(vetorz)

file1=open("saida.dat","w")
for i in range(len(vetorx)):
        linha=str(vetorx[i])+" "+str(vetory[i])+" "+str(vetorz[i])+"\n"
        file1.write(linha)
 
file1.close() 
file.close()

abrir("saida.dat")

import os
lista=[]
term = raw_input('entre com a extensao do arquivo a procurar: ')
print type(term)
a=len(term)
b = -1*a
str(term)
for file in os.listdir("/home/usuario"):
        if (term == file[b:]):
                lista.append(file)
print lista

print
print
print vetorxnp


