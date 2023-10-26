# gerador-de-nomes.py


import random
import base64

nomes = []
sobrenomes = []
sobrenome_completo = []
nome_completo = []

with open('primeiro-nome.txt','r') as fnomes:
    for nome in fnomes.readlines():
        nomes.append(nome.strip())

with open('sobrenomes.txt','r') as fsobrenomes:
    for sobrenome in fsobrenomes.readlines():
        sobrenomes.append(sobrenome.strip('\n'))

for i in range(5555):
    for j in range(random.randint(1,5)):
        
        sobrenome = sobrenomes[random.randint(0,len(sobrenomes)-1)]
        
        if not  sobrenome in sobrenome_completo:
            sobrenome_completo.append(sobrenome)
        else:
            j -= 1
    row = nomes[random.randint(0,len(nomes)-1)] + ' ' + ' '.join(sobrenome_completo)
    nome_completo.append(''.join(row))
    sobrenome_completo = []

for i in range(len(nome_completo)):
    print(nome_completo[i])


