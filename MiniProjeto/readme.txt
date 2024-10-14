Equipe: Wylker Esperidião da Silva

Consultas: 
    - https://hub.asimov.academy/blog/try-except-python/

    - https://gist.github.com/teclad0/a5499c6b558e7d4a1e78518df9f459ca

Consegui realizar todo o código que foi solicitado.

Dificuldades:

    Tive uma dificuldade no tratamento de erros.
    Tinha feito um "class ElementNotFoundError(Exception)" para 
    utilizar na função remove, ao invés de apenas usar o 
    "ValueError". Por isso, passei um bom tempo tentando entender e
    resolver.

    No início também tentei utilizar o parâmetro "queue.data" do 
    arquivo "queueArray.py" porém, não é possível utilizar, pois o
    tipo é retornado como list. 

Desempenho das operações:

    contains(element)
        
        - O(n)
        - É utilizado uma estrutura de repetição para percorrer toda
        a fila e verificar se há o "element" solicitado.

    add(element)

        - O(n)
        - Utilizamos o "contains", que é O(n).

    remove(element)

        - O(n)
        - Também é necessário percorrer toda a fila com uma 
        estrutura de repetição para encontrar o elemento.

    size()

        - O(1)
        - É uma operação constante, pois apenas retorna o tamanho
        atual.

    list()

        - O(n)
        - É necessário percorrer a fila com estruturas de repetição
        para adicionar a lista e remover da fila.

Há formas de melhorar o desempenho do tipo, transformando algumas
funções em O(1), porém é necessário a utilização do "in", que
não foi liberado o uso. Não achei nenhuma outra forma para 
melhorar o desempenho.

