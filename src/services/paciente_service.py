from repositories.paciente_repository import PacienteRepository


class PacienteService:
    def __init__(self):
        self.repository = PacienteRepository()

    def cadastrar(self, paciente):
        self.repository.cadastrar(paciente)

    def listar(self):
        return self.repository.listar()

    def buscar_por_nome(self, nome):
        pacientes = self.repository.listar()
        pacientes_encontrados = []

        for paciente in pacientes:
            if nome.lower() in paciente.nome.lower():
                pacientes_encontrados.append(paciente)

        return pacientes_encontrados