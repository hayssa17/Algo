#Lição 12
def apresentação():
    print('Play')
    print('IaI ! de boa?')
    print('Olá! meu nome é Hayssa e seja bem-vindo ao meu programa!')
   
def número(a,b,c):
    print('Programa em execução...')
    if a > b and a > c:
        print(a,' é maior do que', b, 'e',c )

    elif b > a and b > c:
        print(b,' é maior do que', a, 'e',c )
        

    else:
        print(c,' é maior do que', a, 'e',b )
        
  
    
def fim():
     print('Obrigada por preferir esse programa.')
     
 

apresentação()
    
N1=int(input('Digite um número:'))
N2=int(input('Digite um segundo número:'))
N3=int(input('Digite um terceiro número:'))

número(N1,N2,N3)


    
fim()

