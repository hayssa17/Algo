#lição 8 Meu orgulho!!

def apresentação():
    print('IaI ! de boa?')
    print('Olá! meu nome é Hayssa e seja bem-vindo ao meu programa!')

def mês(num):
      print('Programa em execução...')
      lista=['janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
      num=num-1
      if num < 0 or num > 11:
          print('Mês invalido')
      else:
          print(lista[num])
          

      
    
def fim():
     print('Obrigada por preferir esse programa')          



apresentação()

N=int(input('Digite um número de mês:'))
mês(N)

fim()
