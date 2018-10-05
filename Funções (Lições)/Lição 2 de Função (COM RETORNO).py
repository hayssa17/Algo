#Lição 2 (COM RETORNO)  
def apresentação():
    print('Play')
    print('IaI ! de boa?')
    print('Olá! meu nome é Hayssa e seja bem-vindo ao meu programa!')
   
def número(a):
    print('Programa em execução...')
    if a == 0:
        print('0')
    elif a>0:
        print('1')
    else:
        print('-1')
    return a
   
   
    
def fim():
     print('Obrigada por preferir esse programa')
     
   

apresentação()
    
N=int(input('Digite um número:'))


R = número(N)

    
fim()
