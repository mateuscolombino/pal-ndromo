import numpy as np

def matriza_ant_diagonal(tamanho):
    
    #cria uma transformação linear utilizando uma matriz identidade com a diagonal invertida, invertendo os vetores, ou seja, trocando a última letra com a primeira, e a primeira com a última
    matriz_identidade = np.eye(tamanho)
    matriz_espelho = np.fliplr(matriz_identidade)
    return matriz_espelho

def palavra_vetor(palavra):
    
    #aqui a string vira ASCII(valor numero) pra usar no vetor
    vetor = [ord(letra) for letra in palavra]
    return np.array(vetor)

#aqui começa a magia

frase = input()

#aq tira os espaços e as letras maíusculas 
palavra_boa_pra_usar = frase.replace(" ", "").upper()


tamanhon = len(palavra_boa_pra_usar)

print(f"O computador vai testar: '{palavra_boa_pra_usar}' no espaço vetorial R^{tamanhon}")


#cria uma matriz do tamanho da frase sem os espaços
matriz_T = matriza_ant_diagonal(tamanhon)

#aq a palavra vira um vetor
vetor_v = palavra_vetor(palavra_boa_pra_usar)

# multiplicando T * v
vetor_refletido = matriz_T @ vetor_v


#checando se a matriz é ortogonal com autovalor igual a 1 ; T(v)=1*v
averdade = np.array_equal(vetor_refletido, vetor_v)


if averdade:
    print(f"A entrada '{frase}' é um palíndromo!")   
    print("Ele é um Autovetor associado ao autovalor λ = 1.")
else:
    print(f"A entrada '{frase}' não é um palíndromo.")
    print("T(v) gerou um vetor que aponta pra outra direção no espaço.")