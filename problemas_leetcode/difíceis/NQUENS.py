class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        #cria um conjunto vazio para colunas, diagonal positiva e diagonal negativa
        col = set()
        #A diagonal positiva começa da linha n-1 e os elementos dela são indicados pelo somatório linha + coluna
        posDiag = set()
        #A diagonal negativa começa da 0 e os elementos dela são indicados pelo diferença linha - coluna
        negDiag = set()
        
        #cria uma lista para armazenar as soluções válidas
        resultados = []
        
        #cria o tabuleiro nxn, preenchendo as posições com '.'
        board = [["."] * n for i in range(n)]
        
        #Função recursiva
        def backtrack(r):
            #condição de parada. Quando o algoritmo passar da última linha (as linhas do board vão de 0 a n-1)
            #entendemos que as rainhas foram posicionadas de forma correta e então irá finalizar a recursão
            if r == n:
                copy = ["".join(row) for row in board] #cria uma cópia da configuração atual do tabuleiro. Percorre cada linha do tabuleiro e transforma em string
                resultados.append(copy) #adiciona a cópia à lista de soluções
                return
            
            for c in range(n):
                #esse if confere se é viável colocar uma rainha na coluna c, verificando a coluna c, a diagonal positiva e a diagonal negativa que se originam em c
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue
                
                col.add(c) #adiciona a coluna c ao conjunto col, indicando que uma rainha ocupa essa coluna
                posDiag.add(r + c) #adiciona a diagonal r + c ao conjunto posDiag para indicar que uma rainha ocupa essa diagonal positiva
                negDiag.add(r - c) #adiciona a diagonal r - c ao conjunto negDiag para indicar que uma rainha ocupa essa diagonal negativa
                board[r][c] = "Q" #coloca a rainha na posição [r][c]
                
                backtrack(r + 1) #chama a função recursiva para a próxima linha
                
                #remove a rainha dos conjuntos para liberar para outras tentativas
                col.remove(c) 
                posDiag.remove(r + c) 
                negDiag.remove(r - c)
                board[r][c] = "."
          
        #faz a função começar do 0      
        backtrack(0)
        return resultados
    
"""sol = Solution()

resultados = sol.solveNQueens(1)

for resultado in resultados:
    for linha in resultado:
        print(linha)
    print()"""
        