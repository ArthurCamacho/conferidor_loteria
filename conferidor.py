#Inserir os números sorteados
#Obs: Pode ser também solicitado ao usúario que faça o input manual da lista de números sorteados, além da lista de números jogados
#     Foi desenvolvido dessa forma pois o sroteio de cada concurso é constante, sendo possível alterar somente quando houvesse um novo sorteio
resultado = '01 – 03 – 05 – 07 – 08 – 09 – 10 – 11 – 12 – 15 – 16 – 17 – 20 – 22 – 24'
lista_resultado = set(int(numero) for numero in resultado.split(' – '))

#Criando as variáveis usadas
numeros_jogo = []
quantidade_acertos = 0

#Recebendo os números jogados e transforma a lista em set
for i in range(15):
    numeros_jogo.append(int(input(f'Digite o {i+1}° numero do jogo: ')))
numeros_jogo = set(numeros_jogo)

#Comparando a lista de n° sorteados com a de n° jogados para verificar os acertos
print(f'O jogo teve {len(numeros_jogo.intersection(lista_resultado))} acertos')