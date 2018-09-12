#Lição 5 de lista
N=int(input('Digite a quantidade de números desejadas:'))
L1=[]

soma=0
mult=1

for i in range (0,N):
    Num=int(input('Insira um número:'))
    L1.append(Num)

for i in range (0,N):
    if L1[i]%2==0:
        soma=soma+L1[i]

    else:
        mult=mult*L1[i]

print(L1)
print('Somando os pares da
      :',soma)
print('Multiplicando os impares da:',mult)


        

        
        
    
    
