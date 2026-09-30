from database.conexao import criar_conexao
from models.paciente import Paciente


class PacienteRepository:
    def cadastrar(self, paciente):
        conexao = criar_conexao()
        cursor = conexao.cursor()

        cursor.execute(
            """
            INSERT INTO pacientes (nome, idade, telefone)
            VALUES (?, ?, ?)
            """,
            (paciente.nome, paciente.idade, paciente.telefone)
        )

        conexao.commit()
        conexao.close()

    def listar(self):
        conexao = criar_conexao()
        cursor = conexao.cursor()

        cursor.execute(
            """
            SELECT id, nome, idade, telefone
            FROM pacientes
            """
        )

        registros = cursor.fetchall()
        conexao.close()

        pacientes = []

        for registro in registros:
            paciente = Paciente(
                nome=registro[1],
                idade=registro[2],
                telefone=registro[3],
                id=registro[0]
            )

            pacientes.append(paciente)

        return pacientes