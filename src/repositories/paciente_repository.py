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
            ORDER BY nome
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

    def buscar_por_nome(self, nome):
        conexao = criar_conexao()
        cursor = conexao.cursor()

        cursor.execute(
            """
            SELECT id, nome, idade, telefone
            FROM pacientes
            WHERE nome LIKE ?
            ORDER BY nome
            """,
            (f"%{nome}%",)
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

    def buscar_por_id(self, paciente_id):
        conexao = criar_conexao()
        cursor = conexao.cursor()

        cursor.execute(
            """
            SELECT id, nome, idade, telefone
            FROM pacientes
            WHERE id = ?
            """,
            (paciente_id,)
        )

        registro = cursor.fetchone()
        conexao.close()

        if registro is None:
            return None

        return Paciente(
            nome=registro[1],
            idade=registro[2],
            telefone=registro[3],
            id=registro[0]
        )

    def atualizar(self, paciente):
        conexao = criar_conexao()
        cursor = conexao.cursor()

        cursor.execute(
            """
            UPDATE pacientes
            SET nome = ?, idade = ?, telefone = ?
            WHERE id = ?
            """,
            (
                paciente.nome,
                paciente.idade,
                paciente.telefone,
                paciente.id
            )
        )

        conexao.commit()
        conexao.close()

    def excluir(self, paciente_id):
        conexao = criar_conexao()
        cursor = conexao.cursor()

        cursor.execute(
            """
            DELETE FROM pacientes
            WHERE id = ?
            """,
            (paciente_id,)
        )

        conexao.commit()
        conexao.close()