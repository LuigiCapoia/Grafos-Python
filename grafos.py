import networkx as nx

class Colaborador:
    def __init__(self, nome):
        self.nome = nome

class Departamento:
    def __init__(self, nome, gerente):
        self.nome = nome
        self.gerente = gerente

class Empresa:
    def __init__(self):
        self.grafo = nx.Graph()

    def adicionar_departamento(self, departamento):
        self.grafo.add_node(departamento)

    def adicionar_colaborador(self, colaborador, departamento):
        self.grafo.add_node(colaborador)
        self.grafo.add_edge(colaborador, departamento)

    def obter_colaboradores_por_departamento(self, departamento):
        # Retorna uma lista com os nomes dos colaboradores alocados em um departamento.
        return [node.nome for node in self.grafo.neighbors(departamento) if isinstance(node, Colaborador)]

    def obter_subordinados_por_gerente(self, gerente):
        # Retorna uma lista com os nomes dos colaboradores subordinados a um determinado gerente.
        subordinados = []
        departamentos = [node for node in self.grafo.neighbors(gerente) if isinstance(node, Departamento)]
        for departamento in departamentos:
            colaboradores = self.obter_colaboradores_por_departamento(departamento)
            for colaborador in colaboradores:
              if colaborador != gerente.nome:
                subordinados.append(colaborador)
        return subordinados

    def obter_gerente_e_departamento_por_colaborador(self, colaborador):
        # Retorna o nome do gerente e o departamento em que um colaborador está alocado.
        departamento = [node for node in self.grafo.neighbors(colaborador) if isinstance(node, Departamento)]
        if departamento:
            return departamento[0].gerente.nome, departamento[0].nome
        else:
            return None, None


# Exemplo de utilização do código:

colaboradores = [
    Colaborador("Karen"),
    Colaborador("Akio"),
    Colaborador("Luigi"),
    Colaborador("Polloni"),
    Colaborador("Renan")
]


# Criar departamentos
departamento1 = Departamento("RH", colaboradores[0])
departamento2 = Departamento("TI", colaboradores[2])

# Criar a empresa
empresa = Empresa()
empresa.adicionar_departamento(departamento1)
empresa.adicionar_departamento(departamento2)

# Alocar colaboradores em departamentos
empresa.adicionar_colaborador(colaboradores[0], departamento1)
empresa.adicionar_colaborador(colaboradores[1], departamento1)
empresa.adicionar_colaborador(colaboradores[2], departamento2)
empresa.adicionar_colaborador(colaboradores[3], departamento2)
empresa.adicionar_colaborador(colaboradores[4], departamento2)


# Questão 1: Dado um departamento, mostrar todos os colaboradores alocados nele
departamento = departamento2
colaboradores_departamento = empresa.obter_colaboradores_por_departamento(departamento)
print(f"Colaboradores no departamento {departamento.nome}: {', '.join(colaboradores_departamento)}")


# Questão 2: Dado um gerente, mostrar todos os colaboradores subordinados a ele
gerente = colaboradores[2]
subordinados_gerente = empresa.obter_subordinados_por_gerente(gerente)
print(f"Colaboradores subordinados ao gerente {gerente.nome}: {', '.join(subordinados_gerente)}")


# Questão 3: Dado um colaborador, informe o seu gerente e em qual departamento está alocado
colaborador = colaboradores[3]
gerente, departamento = empresa.obter_gerente_e_departamento_por_colaborador(colaborador)

if gerente and departamento:
    print(f"O colaborador {colaborador.nome} está alocado no departamento {departamento} e seu gerente é {gerente}.")
else:
    print(f"O colaborador {colaborador.nome} não foi encontrado na empresa.")

