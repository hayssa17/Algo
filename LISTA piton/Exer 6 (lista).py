#Lição 6 de lista (completo)
N=int(input('Digite a quantidade de números desejados:'))
L=[]
L2=[]

for i in range (0,N):
    num=int(input('Digite o número desejado:'))
    L.append(num)
print(L)   
    
for cont in range (len(L)-1,-1,-1):
    elemento=L[cont]
    L2.append(elemento)

print(L2)
    

                   
        
    

    
    

    
