#Lição 1 de lista
L=[8,0,97,105,21,303]
M=L[0]
i=0
menor=L[0]
soma=0
Lí=[]
lista=[]
while i < len (L):
    if M<L[i]:
        M=L[i]

    if menor > L[i]:
        menor=L[i]

    soma=soma+L[i]


    if L[i] % 2 !=0:
        Lí.append(L[i])

    if L [i] > 18:
        lista.append (L[i])

    i=i+1

print('Maiores números da lista:',M)
print('Menores números da lista:',menor)
print('sama=',soma)
print('Ímpares:',Lí)
print('Maiores que 18',lista)
