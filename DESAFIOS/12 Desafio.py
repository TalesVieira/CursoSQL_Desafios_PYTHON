#Para este desafio, crie uma lista de frutas e outra de vegetais, use um for loop aninhado para imprimir todas as combinações
#possíveis de frutas e vegetais, com a fruta primeiro e o vegetal em segundo

frutas = ['Maçã', 'Banana', 'Manga', 'Tomate'] # Sim, Tomate é uma fruta.
vegetais = ['Cenoura', 'Alface', 'Ervilha']

for fruta in frutas:
    for vegetal in vegetais:
        print(fruta, vegetal)