class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        # Número total de códigos possíveis
        tamanhoSenha = k**n
        
        # Caminho inicial com n zeros
        caminho = '0' * n
        
        # Conjunto de códigos já visitados
        visitados = set()
        visitados.add(caminho)

        def dfs(caminho: str) -> str:
            # Caso base: se todos os códigos forem visitados, retornamos o caminho
            if len(visitados) == tamanhoSenha:
                return caminho

            # Tentamos adicionar cada dígito de 0 a k-1 ao caminho
            for c in map(str, range(k)):
                # Cria o novo código com o sufixo dos últimos n-1 caracteres + o novo dígito
                novoCodigo = caminho[-n + 1:] + c if n > 1 else c
                
                # Se o novo código não foi visitado, marcamos e chamamos a DFS
                if novoCodigo not in visitados:
                    visitados.add(novoCodigo)
                    resultado = dfs(caminho + c)
                    
                    # Se a DFS retornar um resultado, significa que encontramos a sequência completa
                    if resultado:
                        return resultado
                    
                    # Se a tentativa falhar, removemos o código e tentamos outro
                    visitados.remove(novoCodigo)

        # Inicia a busca e retorna o resultado
        return dfs(caminho)
