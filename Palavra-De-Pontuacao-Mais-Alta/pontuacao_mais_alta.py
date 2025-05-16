def high(x):
    palavras = x.split()
    maior_pontuacao = 0
    melhor_palavra = ""

    for palavra in palavras:
        # Procura a letra na tabela ASCII, subtrai 96 para a ser 1 e não 97
        # Procura a letra na palavra separada da lista palavras
        # Soma tudo e mostra a pontuação

        pontuacao = sum(ord(letra) - 96 for letra in palavra)  

        if pontuacao > maior_pontuacao:
            maior_pontuacao = pontuacao
            melhor_palavra = palavra

    return melhor_palavra

mostrar = print(high('aba abb'))