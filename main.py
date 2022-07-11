from math import inf


capitais = {'Porto Velho':[
                ('Rio Branco',544),
                ('Manaus',901),
                ('Boa Vista',1686),
                ('Cuiabá',1456),
            ],
            'Rio Branco':[('Porto Velho',544)],
            'Boa Vista':[('Porto Velho',1686)],
            'Manaus':[
                ('Palmas',1509),
                ('Porto Velho',901)
            ],
            'Macapá':[
                ('Belém',1000),
            ],
            'Belém':[
                ('Macapá',1000),
                ('São Luís',1610),
                ('Palmas',1610)
            ],
            'São Luís':[
                ('Belém',1610),
                ('Teresina',446),
                ('Palmas',964),
            ],
            'Palmas':[
                ('Belém',973),
                ('Teresina',1401),
                ('São Luís',964),
                ('Cuiabá',1029),
                ('Brasília',620),
            ],
            'Cuiabá':[
                ('Porto Velho',1456),
                ('Palmas',620),
                ('Goiânia',934),
                ('Campo Grande',934),
            ],
            'Goiânia':[
                ('Cuiabá',934),
                ('Campo Grande',935),
                ('Brasília',209),
                ('Belo Horizonte',906),
            ],
            'Brasília':[
                ('Goiânia',209),
                ('Palmas',973),
                ('Salvador',1443),
                ('Fortaleza',2200),
            ],
            'Fortaleza':[
                ('Teresina',634),
                ('Brasília',2200),
                ('Salvador',1389),
                ('Aracajú',815),
                ('Maceió',1075),
                ('Recife',800),
                ('João Pessoa',688),
                ('Natal',537)
            ],
            'Campo Grande':[
                ('Cuiabá',694),
                ('Goiânia',935),
                ('Belo Horizonte',935),
                ('Curitiba',991)
            ],
            'Natal':[
                ('João Pessoa',151),
                ('Fortaleza',537)
            ],
            'João Pessoa':[
                ('Natal',151),
                ('Recife',120),
                ('Fortaleza',688)
            ],
            'Recife':[
                ('João Pessoa',120),
                ('Maceió',202),
                ('Fortaleza',800)
            ],
            'Maceió':[
                ('Recife',202),
                ('Aracajú',201),
                ('Fortaleza',1075),
            ],
            'Aracajú':[
                ('Salvador',356),
                ('Maceió',201),
                ('Fortaleza',815),
            ],
            'Salvador':[
                ('Brasília',1060),
                ('Aracajú',356),
                ('Fortaleza',1389),
            ],
            'Belo Horizonte':[
                ('Vitória',524),
                ('Goiânia',906),
                ('Campo Grande',906),
                ('Rio de Janeiro',906),
                ('São Paulo',586)
            ],
            'Vitória':[
                ('Belo Horizonte',524),
                ('Rio de Janeiro',741)
            ],
            'Rio de Janeiro':[
                ('Vitória',741),
                ('Belo Horizonte',906),
                ('São Paulo',429)
            ],
            'São Paulo':[
                ('Rio de Janeiro',429),
                ('Belo Horizonte',586),
                ('Curitiba',338),
            ],
            'Curitiba':[
                ('Florianópolis',300),
                ('Campo Grande',780),
                ('São Paulo',338),
                ('Porto Alegre',546),
            ],
            'Florianópolis':[
                ('Curitiba',300),
                ('Porto Alegre',376),
            ],
            'Porto Alegre':[
                ('Florianópolis',376),
                ('Curitiba',546),
            ],
}

class GraphModel():
    
    def __init__(self, edges: dict) -> None: 
        """
        Init graph as a dictionary
        edges = {
          "A": [("B", dist_AB),("C", dist_AC)],]
          "B": [("A", dist_AB)]
        }
        """
        self.graph = dict
        self.add_edges(edges)
        self.add_adjacent_nodes(edges)
    
    def add_edges(self, edges: dict) -> None:
        """
        Add edges to graph as dictionary of lists        
        """
        self.graph = edges
    
    def add_adjacent_nodes(self, edges: dict) -> None:
        """
        Create a dict with adjacent_nodes
        adjacent_nodes = {
          "A" = { "B": dist_AB, "C": dist_AC },
          "B" = { "C": dist_BC }
        }
        """
        self.adjacent_nodes = dict()
        
        for key in edges:
          self.adjacent_nodes[key] = dict()

          for x in edges[key]:
            self.adjacent_nodes[key][x[0]] = x[1]

    def get_edges(self) -> None:
        """
        Returns all graph's edges
        """
        edges = []
        for key in self.graph.keys():
            edges.append((key, self.graph[key]))
        return edges

    def get_nodes(self) -> list:
        """
        Returns all graph's nodes
        """
        return list(self.graph.keys())

    def get_neighbors(self) -> dict:
        """
        Returns all neighbors from graph
        """
        return self.graph

    def find_shortest_path(self, start: str, end: str) -> list:
        """
        Find shortest path using Dijkstra algorithm
        """
        path = [end] # path will be backwards in first moment
        total_dist = 0 # total distance traveled
        dijkstra_result = self.dijkstra(start=start)

        total_dist, node = dijkstra_result.get(end) # init path and set total distance by end point

        # path finder (end node to start node)
        while node != start:
          path.append(node)
          dist, node = dijkstra_result.get(node)
        
        path.append(start) # add start node at the end
        path.reverse() # correct path to be start point to end point

        return (path, total_dist)


    def dijkstra(self, start):
        """
        Dijkstra algorithm
        return = {
          node_A: (min_dist, min_neighbor),
          node_B: (min_dist, min_neighbor)
        }
        """
        nodes = self.get_nodes()
        distances = {}

        # init distances with infinite and 0 to start point
        for node_A in self.adjacent_nodes:
          for node_B in self.adjacent_nodes[node_A]:
            distances[node_A] = (inf, None)
            distances[node_B] = (inf, None)
        distances[start] = (0, start)

        # init not visited nodes list
        temporary_nodes = [n for n in nodes]

        # while temporary nodes is not empty
        while len(temporary_nodes) > 0:
            upper_bounds = {n: distances[n] for n in temporary_nodes}
            lower_bound = min(upper_bounds, key=lambda v: upper_bounds.get(v)[0])
            temporary_nodes.remove(lower_bound)
            for node, distance in self.adjacent_nodes[lower_bound].items():
                new_distance = (distances[lower_bound][0] + distance, lower_bound)
                distances[node] = min(distances[node], new_distance, key=lambda v:v[0])

        return distances

capitais_lista = [
    'Manaus',
    'Rio Branco',
    'Campo Grande',
    'Macapá',
    'Brasília',
    'Boa Vista',
    'Cuiabá',
    'Palmas',
    'São Paulo',
    'Teresina',
    'Rio de Janeiro',
    'Belém',
    'Goiânia',
    'Salvador',
    'Florianópolis',
    'São Luís',
    'Maceió',
    'Porto Alegre',
    'Curitiba',
    'Belo Horizonte',
    'Fortaleza',
    'Recife',
    'João Pessoa',
    'Aracajú'
]

capitais_lista = sorted(capitais_lista)

def printa_capitais():
    for capital in range(len(capitais_lista)):
        print(f"{capital} - {capitais_lista[capital]}")


def menu():
    print("Welcome to Capital Traveler!!")
    print("There youu go !!\nChoose One Brazil's Capital as a starting point!")

    printa_capitais()

    start = int(input("Escolha : "))
    start = capitais_lista[start]

    end = int(input("Now choose the ending capital : "))
    end = capitais_lista[end]

    return start,end

def shortest_path(graph,start,end):
    bala = graph.find_shortest_path(start,end)
    return bala    

def main():
    # declaração do grafo
    graph = GraphModel(edges=capitais)
    # start end
    start,end = menu()

    bala = shortest_path(graph,start,end)

    print("The shortest path is : \n")
    print(bala[0])
    print(f"With the total distance of : {bala[1]}\n\n")

    again = int(input("Do you want to travel again ?\n1 - Yes\n0 - No\n:: "))
    if again == 1:
        main()

if __name__ == "__main__":
    main()