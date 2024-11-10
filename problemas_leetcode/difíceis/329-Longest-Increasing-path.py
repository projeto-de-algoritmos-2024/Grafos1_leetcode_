class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        
        #Tentarei resolver esse exercício com busca em profundidade
        """
        DFS(G)
            1 Para todo v em G:
            2   Se v não visitado então
            3       DFS-Visit(G, v)
        DFS-Visit(G, v)
            1 Marque v como visitado
            2 Para todo w em Adj(v):
            3   Se w não visitado então
            4       Insira aresta (v, w) na árvore
            5       DFS-Visit(G, w)
        """ 
        # Algoritmo aplicado a python:
        """
        def dfs(graph):
            visited = set()  # Conjunto para marcar vértices visitados
            
            def dfs_visit(node):
                visited.add(node)
                print(node, end=' ')  # Imprime o vértice visitado (opcional)
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        dfs_visit(neighbor)
                        
            # Inicia a DFS a partir de cada vértice não visitado
            for node in graph:
                if node not in visited:
                    dfs_visit(node)
        """
        
        #Algoritmo da resolução do problema:
        linhas, colunas = len(matrix), len(matrix[0])
        dp = {}  # Dicionário para armazenar os resultados das subsoluções

        def visitar_dfs(linha, coluna, valor_anterior):
            # Verificar se está fora dos limites ou se o valor não está aumentando
            if (linha < 0 or linha == linhas or coluna < 0 or coluna == colunas or matrix[linha][coluna] <= valor_anterior):
                return 0

            # Retornar o resultado armazenado, se existir
            if (linha, coluna) in dp:
                return dp[(linha, coluna)]

            # Inicializar o comprimento máximo com 1 (a célula atual)
            resultado = 1

            # Explorar todas as quatro direções
            resultado = max(resultado, 1 + visitar_dfs(linha + 1, coluna, matrix[linha][coluna]))  # Abaixo
            resultado = max(resultado, 1 + visitar_dfs(linha - 1, coluna, matrix[linha][coluna]))  # Acima
            resultado = max(resultado, 1 + visitar_dfs(linha, coluna + 1, matrix[linha][coluna]))  # Direita
            resultado = max(resultado, 1 + visitar_dfs(linha, coluna - 1, matrix[linha][coluna]))  # Esquerda

            # Armazenar o resultado no dicionário dp
            dp[(linha, coluna)] = resultado
            return resultado

        # Iniciar a DFS em todas as células da matriz
        for linha in range(linhas):
            for coluna in range(colunas):
                visitar_dfs(linha, coluna, -1)  # Começar com um valor menor que qualquer célula

        # Retornar o caminho mais longo encontrado
        return max(dp.values())