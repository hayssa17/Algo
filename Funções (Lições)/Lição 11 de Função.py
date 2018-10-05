#Lição 11
def apresentação():
    print('Play')
    print('IaI ! de boa?')
    print('Olá! meu nome é Hayssa e seja bem-vindo ao meu programa!')
   
def número(a,b):
    print('Programa em execução...')
    if a > b:
        print(a,' é maior do que', b )
    else:
        print(b,' é maior do que', a )
    
def fim():
     print('Obrigada por preferir esse programa')
     
    
               


apresentação()
    
N1=int(input('Digite um número:'))
N2=int(input('Digite um número:'))

número(N1,N2)


    
fim()

