class Paciente:
    def __init__(self, nome, idade, telefone, id=None):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.telefone = telefone