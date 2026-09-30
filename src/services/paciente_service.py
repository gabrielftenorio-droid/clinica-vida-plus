class PacienteService:
    def __init__(self):
        self.pacientes = []

    def cadastrar(self, paciente):
        self.pacientes.append(paciente)

    def listar(self):
        return self.pacientes

    def buscar_por_nome(self, nome):
        pacientes_encontrados = []

        for paciente in self.pacientes:
            if nome.lower() in paciente.nome.lower():
                pacientes_encontrados.append(paciente)

        return pacientes_encontrados