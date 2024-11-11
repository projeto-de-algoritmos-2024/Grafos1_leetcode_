class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        
        # Passo 1: Inicializar as distâncias: todas infinitas, exceto a origem que é zero
        distancias = [float("inf")] * n
        distancias[src] = 0

        # Passo 2: Relaxar as arestas até k + 1 vezes (permitindo no máximo k paradas)
        for i in range(k + 1):
            # Criar uma cópia para evitar atualizações prematuras
            novas_distancias = distancias[:]
            for origem, destino, preco in flights:
                if distancias[origem] != float('inf') and distancias[origem] + preco < novas_distancias[destino]:
                    novas_distancias[destino] = distancias[origem] + preco
            distancias = novas_distancias
            
        # Passo 3 não é necessária para esse problema, pois estamos lidando com um número finito de paradas e um grafo com custos não negativos.
        
        # Verifica se o destino é alcançável
        return distancias[dst] if distancias[dst] != float('inf') else -1
