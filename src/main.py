from models.paciente import Paciente
from services.paciente_service import PacienteService


def cadastrar_paciente(paciente_service):
    nome = input("Nome: ").strip()

    while True:
        try:
            idade = int(input("Idade: "))
            break
        except ValueError:
            print("Idade inválida. Digite apenas números.")

    telefone = input("Telefone: ").strip()

    paciente = Paciente(nome, idade, telefone)

    try:
        paciente_service.cadastrar(paciente)
        print("Paciente cadastrado com sucesso.")
    except ValueError as erro:
        print(erro)


def listar_pacientes(paciente_service):
    pacientes = paciente_service.listar()

    if not pacientes:
        print("Nenhum paciente cadastrado.")
        return

    print("\nPacientes cadastrados:")

    for paciente in pacientes:
        print(f"ID: {paciente.id}")
        print(f"Nome: {paciente.nome}")
        print(f"Idade: {paciente.idade}")
        print(f"Telefone: {paciente.telefone}")
        print()


def buscar_paciente(paciente_service):
    nome = input("Digite o nome do paciente: ").strip()

    pacientes_encontrados = paciente_service.buscar_por_nome(nome)

    if not pacientes_encontrados:
        print("Nenhum paciente encontrado.")
        return

    print("\nPacientes encontrados:")

    for paciente in pacientes_encontrados:
        print(f"ID: {paciente.id}")
        print(f"Nome: {paciente.nome}")
        print(f"Idade: {paciente.idade}")
        print(f"Telefone: {paciente.telefone}")
        print()


def atualizar_paciente(paciente_service):
    try:
        paciente_id = int(input("Digite o ID do paciente: "))
    except ValueError:
        print("ID inválido.")
        return

    paciente = paciente_service.buscar_por_id(paciente_id)

    if paciente is None:
        print("Paciente não encontrado.")
        return

    print(f"\nPaciente: {paciente.nome}")

    nome = input(f"Novo nome [{paciente.nome}]: ").strip()

    if nome:
        paciente.nome = nome

    idade = input(f"Nova idade [{paciente.idade}]: ").strip()

    if idade:
        try:
            paciente.idade = int(idade)
        except ValueError:
            print("Idade inválida. Alteração cancelada.")
            return

    telefone = input(f"Novo telefone [{paciente.telefone}]: ").strip()

    if telefone:
        paciente.telefone = telefone

    try:
        paciente_service.atualizar(paciente)
        print("Paciente atualizado com sucesso.")
    except ValueError as erro:
        print(erro)


def excluir_paciente(paciente_service):
    try:
        paciente_id = int(input("Digite o ID do paciente: "))
    except ValueError:
        print("ID inválido.")
        return

    paciente = paciente_service.buscar_por_id(paciente_id)

    if paciente is None:
        print("Paciente não encontrado.")
        return

    print(f"Paciente encontrado: {paciente.nome}")

    confirmacao = input(
        "Deseja realmente excluir este paciente? (s/n): "
    ).strip().lower()

    if confirmacao == "s":
        paciente_service.excluir(paciente_id)
        print("Paciente excluído com sucesso.")
    else:
        print("Exclusão cancelada.")


paciente_service = PacienteService()

while True:
    print("\nClínica Vida+")
    print("1. Cadastrar paciente")
    print("2. Listar pacientes")
    print("3. Buscar paciente")
    print("4. Atualizar paciente")
    print("5. Excluir paciente")
    print("6. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_paciente(paciente_service)

    elif opcao == "2":
        listar_pacientes(paciente_service)

    elif opcao == "3":
        buscar_paciente(paciente_service)

    elif opcao == "4":
        atualizar_paciente(paciente_service)

    elif opcao == "5":
        excluir_paciente(paciente_service)

    elif opcao == "6":
        print("Encerrando o sistema...")
        break

    else:
        print("Opção inválida.")