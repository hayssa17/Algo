#Lição 14
def apresentação():
    print('Play')
    print('IaI ! de boa?')
    print('Olá! meu nome é Hayssa e seja bem-vindo ao meu programa!')
   
def número(K,V):
    print('Programa em execução...')
    a_ser_recebido=V*K
    print(a_ser_recebido,'$')
  
    
def fim():
     print('Obrigada por preferir esse programa')
     
   

apresentação()
    
Km=int(input('Digite quantos quilometros foram: '))
valor=int(input('Digite o valor do desconto á ser aplicado:'))


número(Km,valor)


    
fim()
