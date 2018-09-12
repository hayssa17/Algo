#Lição 3 de lista
N=int(input('Digite o número de notas que serão colocadas:'))
No=N
L=[]
soma=0

while N > 0:
    nota=float(input('Digite a nota do aluno:'))
    L.append(nota)
    soma=soma+nota
    

    N=N-1
media=soma/No

print(media)
    
    
