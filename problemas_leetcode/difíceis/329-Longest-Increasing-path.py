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