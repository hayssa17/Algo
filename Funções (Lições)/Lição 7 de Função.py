#Lição 7 
def apresentação():
    print('IaI ! de boa?')
    print('Olá! meu nome é Hayssa e seja bem-vindo ao meu programa!')
   
def número(num):
    print('Programa em execução...')
    if num >=0:
        print(num,'é um número positivo.')
    else:
        print(num,'é um número negativo.')

    
    
    
def fim():
     print('Obrigada por preferir esse programa')
     
    
               

print('Play')
apresentação()
    
N=float(input('digite um número:'))

número(N)

    
fim()


