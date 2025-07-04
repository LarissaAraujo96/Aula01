#Treinando o if e else

idade = int(input('Qual a sua idade?'))
if  idade >= 18:
    print("Você é maior de idade")
else:
    print('Você é de menor')


numero1 = int(input('Digite um numero'))
if numero1 <10:
    print('Este numero é menor')
else:
    print('Este numero é maior')


numero2 = int(input('Digite um numero'))
if numero2 ==5:
    print('Este nuemro esta correto')
else:
    print ('Este numero esta incorreto')


numero = int(input('Digite um numero para verificar se é impar ou par'))
par = numero%2

if (par ==0 ):
    print('Este numero é par')
else:
    ('Este nuemro pe impar')


numero4 = int(input('Digite um numero'))
if numero4 <= 5:
    print('Este numero é menor')
else: 
    print('Este numero é maior')
    

numero5 = int(input('Digite um numero maior que 5'))
if numero5 >= 5:
    print("Este nuemro é maior")
elif numero ==5:
    print('Este numero é igual a 5')
else:
    print('Este numero pe menor que cinco')


numero6 = int(input("Qual o numero da sorte?"))
if numero6 >=10:
    print('Legal, seu numero é maior que 10')
elif numero6 ==10:
    print('Legal, seu nuemro é 10')
else:
    print('Legal, seu numero é menor que 10')


#concatenar com f
numero7 = float(input('Digite um numero para soma'))
numero8 = float(input('Digite um numero para soma'))
resultado = numero7+numero8
print(f'O resultado de {numero7} mias {numero8} é {resultado}')

print ('Programa para saber se pode tirar a CNH')
pessoa = input('Digite seu nome')
idade = int(input('Quanto anos você tem?'))
if idade >=18:
    print(f'Parabens {pessoa} você ja tem {idade}anos e ja pode dirigir')
else:
    print(f'{pessoa} infelismente você ainda não pode dirigir')

#1-branco
#2-verde
#3-vermelho

print('Validação de voto')
pessoa = input('Digite seu nome')
voto = int(input ('Digite o seu voto: 1, 2 ou 3'))
if voto == 1:
    print (f'{pessoa}, você votou branco')
elif voto ==2:
    print (f'{pessoa}, você votou verde')
elif voto ==3:
    print (f'{pessoa}, você votou vermelho')
else:
    print ('você votou errado')
    print('Obrigado pelo seu voto')