class Colaborador:
    def __init__(self, nome):
        self.nome = nome
        self.departamento = None
        self.gerente = None

class Departamento:
    def __init__(self, nome, gerente):
        self.nome = nome
        self.gerente = gerente
        self.colaboradores = []

    def adicionar_colaborador(self, colaborador):
        self.colaboradores.append(colaborador)

class Empresa:
    def __init__(self):
        self.departamentos = {}

    def adicionar_departamento(self, departamento):
        self.departamentos[departamento.nome] = departamento

         

    def obter_colaboradores_por_departamento(self, departamento):
        # Retorna uma lista com os nomes dos colaboradores alocados em um departamento.
        if departamento in self.departamentos:
            return [colaborador.nome for colaborador in self.departamentos[departamento].colaboradores]
        else:
            return []

    def obter_subordinados_por_gerente(self, gerente):
        # Retorna uma lista com os nomes dos colaboradores subordinados a um determinado gerente.
        subordinados = []
        for departamento in self.departamentos.values():
            if departamento.gerente.nome == gerente:
                subordinados.extend([colaborador.nome for colaborador in departamento.colaboradores if colaborador.nome != gerente])
        return subordinados

    def obter_gerente_e_departamento_por_colaborador(self, colaborador):
        # Retorna o nome do gerente e o departamento em que um colaborador está alocado.
        for departamento in self.departamentos.values():
            if colaborador in [colab.nome for colab in departamento.colaboradores]:
                return departamento.gerente.nome, departamento.nome
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

# Alocar colaboradores em departamentos
departamento1.adicionar_colaborador(colaboradores[0])
departamento1.adicionar_colaborador(colaboradores[1])
departamento2.adicionar_colaborador(colaboradores[2])
departamento2.adicionar_colaborador(colaboradores[3])
departamento2.adicionar_colaborador(colaboradores[4])

# Criar a empresa
empresa = Empresa()
empresa.adicionar_departamento(departamento1)
empresa.adicionar_departamento(departamento2)




# Questão 1: Dado um departamento, mostrar todos os colaboradores alocados nele
departamento = "TI"
colaboradores_departamento = empresa.obter_colaboradores_por_departamento(departamento)
print(f"Colaboradores no departamento {departamento}: {', '.join(colaboradores_departamento)}")

# Questão 2: Dado um gerente, mostrar todos os colaboradores subordinados a ele
gerente = "Luigi"
subordinados_gerente = empresa.obter_subordinados_por_gerente(gerente)
print(f"Colaboradores subordinados ao gerente {gerente}: {', '.join(subordinados_gerente)}")


# Questão 3: Dado um colaborador, informe o seu gerente e em que departamento está alocado
colaborador = "Polloni"
gerente, departamento = empresa.obter_gerente_e_departamento_por_colaborador(colaborador)

if gerente and departamento:
    print(f"O colaborador {colaborador} está alocado no departamento {departamento} e seu gerente é {gerente}.")
else:
    print(f"O colaborador {colaborador} não foi encontrado na empresa.")
