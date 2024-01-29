'''
Problema do Zelador Eficiente

O zelador de uma faculdade é extremamente eficiente. Ao final de cada dia, todo 
o lixo da escola está em sacos plásticos com peso entre 1,01 e 3,00 quilos. 
Então, todas as sacolas plásticas são levadas para as lixeiras do lado de fora. 
Uma viagem é descrita como selecionar um número de sacolas que juntas não pesam 
mais de 3,00 quilos, despejá-las na lixeira externa e retornar à faculdade. 
Dado o número de sacolas plásticas n e o peso de cada sacola, determine o número 
mínimo de viagens que o zelador deve fazer.

Descrição do formato da função solução

1) Recebe como parâmetro um vetor com o peso das sacolas a serem levadas.
2) Retorne a quantidade de viagens que o zelador deve fazer.

Exemplos

Exemplo 1:
Entrada: pesos = [1.01, 1.99, 2.5, 1.5, 1.01]
Saída: 3
Explicação: O zelador consegue levar todas as sacolas plásticas em 3 viagens: 
[1,01 + 1,99 , 2,5, 1,5 + 1,01].

Exemplo 2:
Entrada: pesos = [1.01, 1.01, 1.01, 1.4]
Saída: 2
'''

def main(garbages):
    travel_content = []
    travel_count = 1
    for garb in garbages:
        print(f'Travel content -> {travel_content} | total weight {sum(travel_content)}')
        if sum(travel_content) + garb <= 3:
            travel_content.append(garb)
        else:
            print(f'Adding {garb} to new travel')
            travel_content = [garb]
            travel_count += 1

    return travel_count

if __name__ == '__main__':
    pesos = [
        ([1.01, 1.99, 2.5, 1.5, 1.01], 3),
        ([1.01, 1.01, 1.01, 1.4], 2),
    ]

    for peso in pesos:
        assert main(peso[0]) == peso[1]