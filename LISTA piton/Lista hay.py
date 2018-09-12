
#Questão a
Lista=['pera','uva','laranja','mamão','banana']

print(Lista[2])

#Questão b
Lista.append('limão')
Lista.append(104)
print(Lista)



# Questão c
i=0
while Lista[i]!= 'mamão':
    i+=1

print(i)
    
     
        

#Questão d

Lista[3]='pera'


#Questão e

cont=0

for fruta in Lista:
    if fruta=='pera':
        cont+=1
print('A Palavra Pera aparece',cont,'vezes nessa lista')

#Questão f

print(Lista[0]+Lista[4])

#Questão g

del Lista[1]
print(Lista)

#Questão h

print(len (Lista))
