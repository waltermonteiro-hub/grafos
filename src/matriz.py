import sys
from abc import ABC, abstractmethod

class Grafo(ABC):
    @abstractmethod
    def numero_de_vertices(self):
        pass

    @abstractmethod
    def numero_de_arestas(self):
        pass

    @abstractmethod
    def sequencia_de_graus(self):
        pass

    @abstractmethod
    def adicionar_aresta(self, u, v):
        pass

    @abstractmethod
    def remover_aresta(self, u, v):
        pass

    @abstractmethod
    def imprimir(self):
        pass


class GrafoDenso(Grafo):
    # Definição do grafo
    def __init__(self, num_vertices=None, labels=None):
        if labels:
            self.labels = labels
            self.num_vertices = len(labels)
            self.mapa_labels = {label: i for i, label in enumerate(labels)}
        elif num_vertices:
            self.num_vertices = num_vertices
            self.labels = [str(i) for i in range(num_vertices)]
            self.mapa_labels = {str(i): i for i in range(num_vertices)}
        else:
            print("Erro: Forneça 'num_vertices' ou uma lista de 'labels'.")
            sys.exit(1)

        # Cria a matriz de adjacência NxN preenchida com zeros
        self.matriz = [[0] * self.num_vertices for i in range(self.num_vertices)]
        
    
    def numero_de_vertices(self):
        # Retorna o número total de vértices no grafo.
        return self.num_vertices

    def numero_de_arestas(self):
        # Retorna o número total de arestas no grafo.
        count = 0
        for i in range(self.num_vertices):
            for j in range(i + 1, self.num_vertices):
                if self.matriz[i][j] != 0:
                    count += 1
        return count

    def sequencia_de_graus(self):
        # Retorna uma lista com os graus de todos os vértices.
        return sorted([sum(row) for row in self.matriz])


    def _obter_indice(self, vertice):
        if isinstance(vertice, str) and vertice in self.mapa_labels:
            return self.mapa_labels[vertice]
        elif isinstance(vertice, int) and 0 <= vertice < self.num_vertices:
            return vertice
        else:
            raise ValueError(f"Vértice '{vertice}' é inválido.")


    def adicionar_aresta(self, u, v):
        """
        Adiciona a aresta entre os vértices u e v.
        """
        try:
            idx_u = self._obter_indice(u)
            idx_v = self._obter_indice(v)

            self.matriz[idx_u][idx_v] = 1
            self.matriz[idx_v][idx_u] = 1

            print(f"Aresta adicionada entre {u} e {v}.")
        except ValueError as e:
            print(f"Erro ao adicionar aresta: {e}")


    def remover_aresta(self, u, v):
        """
        Remove a aresta entre os vértices u e v.
        """
        try:
            idx_u = self._obter_indice(u)
            idx_v = self._obter_indice(v)

            if self.matriz[idx_u][idx_v] == 0:
                print(f"Aresta entre {u} e {v} não existe.")
                return

            # Remove a aresta
            self.matriz[idx_u][idx_v] = 0
            self.matriz[idx_v][idx_u] = 0
            print(f"Aresta removida entre {u} e {v}.")
        
        except ValueError as e:
            print(f"Erro ao remover aresta: {e}")

    def imprimir(self):
        """Imprime a matriz de adjacência de forma legível."""
        print("\nMatriz de Adjacência:")
        # Imprime o cabeçalho das colunas
        header = "   " + "  ".join(self.labels)
        print(header)
        print("─" * len(header))

        # Imprime as linhas com seus respectivos rótulos
        for i, linha in enumerate(self.matriz):
            print(f"{self.labels[i]} |", "  ".join(map(str, linha)))
        print()
