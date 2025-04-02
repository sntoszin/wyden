
1. Vetores (Arrays): Vetores, ou arrays, são estruturas de dados que armazenam elementos do mesmo tipo em posições contíguas de memória. Eles permitem o acesso direto aos elementos por meio de índices.​
growthcode.com.br

Exemplo: Um vetor que armazena as idades de cinco pessoas:

    idades = [25, 30, 35, 40, 45]
    print(idades[2]) 

2. Matrizes (Arrays Multidimensionais): Uma matriz multidimensional é uma matriz cujos elementos são matrizes. Por exemplo, o primeiro elemento de uma matriz tridimensional é uma matriz com duas dimensões.

Exemplo: Uma matriz 2x3 que representa notas de alunos em duas disciplinas:
notas = [

    [7.5, 8.0, 9.0],  
    [6.5, 7.0, 8.0]   
]

    print(notas[1][2])  # Saída: 8.0

3.  Listas: Listas são estruturas de dados lineares que podem armazenar elementos de tipos diferentes e têm tamanho dinâmico, ou seja, podem crescer ou diminuir conforme necessário.​

Exemplo: Uma lista que contém nomes de frutas:
frutas = 

    ["Maçã", "Banana", "Cereja"]
    frutas.append("Damasco") 
    print(frutas[1])  

4. Pilha (Stack): Uma pilha é uma estrutura de dados do tipo LIFO (Last In, First Out), onde o último elemento a ser inserido é o primeiro a ser removido.

Exemplo: Uma pilha de livros onde o último livro colocado é o primeiro a ser retirado:
livros = []

    livros.append("Livro A")  
    livros.append("Livro B") 
    print(livros.pop())       

5. Fila (Queue): Uma fila é uma estrutura de dados do tipo FIFO (First In, First Out), onde o primeiro elemento a ser inserido é o primeiro a ser removido.​

Exemplo: Uma fila de atendimento em um caixa de supermercado:
from collections import deque

    fila = deque(["Cliente 1", "Cliente 2", "Cliente 3"])
    fila.append("Cliente 4") 
    print(fila.popleft()) 

6. Tuplas: Tuplas são estruturas de dados semelhantes às listas, mas são imutáveis, ou seja, seus elementos não podem ser alterados após a criação.​
   
Exemplo: Uma tupla que representa as coordenadas de um ponto no plano cartesiano:

    ponto = (3, 5)
    print(ponto[0])  # Saída: 3

7. Conjuntos (Sets): Conjuntos são coleções não ordenadas de elementos únicos, ou seja, não permitem duplicatas.​

   Exemplo: Um conjunto de números primos menores que 10:

        numeros_primos = {2, 3, 5, 7}
        numeros_primos.add(11)  
        print(3 in numeros_primos)

