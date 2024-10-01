#Neste desafio, quero que você crie um script que solicite ao usuário dois números. Em seguida, seu script deve imprimir
#A soma, a subtração, a multiplicação, a adivisão e a exponenciação desses dois números.

n1 =int(input('Digite o primero número: '))
n2 =int(input('Digite o segundo número: '))

soma = n1 + n2
subtração = n1 - n2
multiplicação = n1 * n2
divisão = n1 / n2
exponenciação = n1 ** n2

print(f'A soma dos dois valores digitados é de {soma}!')
print(f'A subtração dos dois valores digitados é igual a  {subtração}!')
print(f'A multiplicação dos dois valores digitados é igual a {multiplicação}!')
print(f'A divisão dos dois valores digitados é de {divisão:.2f}!')
print(f'A exponenciação dos dois valores digitados é {exponenciação}')