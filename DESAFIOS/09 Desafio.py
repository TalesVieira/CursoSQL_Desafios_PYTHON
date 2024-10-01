#Para este desafio, comece com a lista 'frutas' do desafio anterior, primeiro remova a "manga" da lista usando o método remove(), depois
#remova o último item da lista usando o comando del, por fim imprima a lista modificada na tela
frutas = ['Maçã', 'Morango', 'Manga', 'Uva', 'Abacaxi']

frutas.remove('Manga')
del frutas[-1]
print(frutas)