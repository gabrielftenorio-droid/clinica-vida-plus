from repositories.paciente_repository import PacienteRepository


class PacienteService:
    def __init__(self):
        self.repository = PacienteRepository()

    def cadastrar(self, paciente):
        if not paciente.nome.strip():
            raise ValueError("O nome do paciente é obrigatório.")

        if paciente.idade < 0 or paciente.idade > 120:
            raise ValueError("A idade deve estar entre 0 e 120 anos.")

        if not paciente.telefone.strip():
            raise ValueError("O telefone do paciente é obrigatório.")

        self.repository.cadastrar(paciente)

    def listar(self):
        return self.repository.listar()

    def buscar_por_nome(self, nome):
        return self.repository.buscar_por_nome(nome)

    def buscar_por_id(self, paciente_id):
        return self.repository.buscar_por_id(paciente_id)

    def atualizar(self, paciente):
        if not paciente.nome.strip():
            raise ValueError("O nome do paciente é obrigatório.")

        if paciente.idade < 0 or paciente.idade > 120:
            raise ValueError("A idade deve estar entre 0 e 120 anos.")

        if not paciente.telefone.strip():
            raise ValueError("O telefone do paciente é obrigatório.")

        self.repository.atualizar(paciente)

    def excluir(self, paciente_id):
        self.repository.excluir(paciente_id)