#Lição 1 (COM RETORNO)  
def apresentação():
    print('Play')
    print('IaI ! de boa?')
    print('Olá! meu nome é Hayssa e seja bem-vindo ao meu programa!')
   
def número(a,b,c):
    print('Programa em execução...')
    R=a+b+c
    return R
   
   
    
def fim():
     print('Obrigada por preferir esse programa')
     
   

apresentação()
    
N1=int(input('Digite um número:'))
N2=int(input('Digite Outro número:'))
N3=int(input('Digite um terceiro número:'))

R = número(N1,N2,N3)
print(N1,'+',N2,'+',N3,'=',R)

    
fim()
