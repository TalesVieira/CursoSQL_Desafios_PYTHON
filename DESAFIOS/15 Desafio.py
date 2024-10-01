#Para este desafio crie uma lista de frutas que inclui maçã 3 vezes e outras frutas de sua escolha use um loop for para contar quantas vezes
# maçã aparece na lista e imprima o resultad
frutas = ['maçã', 'banana', 'maçã', 'uva' 'abacaxi' 'tomate' 'maçã']
contador = 0

for fruta in frutas:
    if fruta == 'maçã':
        contador +=1

print(f'A lista possui {contador} maçãs')