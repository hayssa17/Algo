#Llição 4 de lista
N=int(input('Digite o número de notas que serão colocadas:'))
L1=[]
L2=[]


while N > 0:
    nota=int(input('Digite a nota do aluno:'))
    L1.append(nota)
   
    N=N-1

i=0
while i < len(L1):
    if L1[i] not in L2:
        L2.append(L1[i])
    i=i+1


print(L1)
print(L2)
    
    
