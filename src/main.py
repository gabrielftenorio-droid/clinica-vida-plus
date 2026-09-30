from models.paciente import Paciente
from services.paciente_service import PacienteService


def cadastrar_paciente(paciente_service):
    nome = input("Nome: ")

    while True:
        try:
            idade = int(input("Idade: "))
            break
        except ValueError:
            print("Idade inválida. Digite apenas números.")

    telefone = input("Telefone: ")

    paciente = Paciente(nome, idade, telefone)
    paciente_service.cadastrar(paciente)

    print("Paciente cadastrado com sucesso.")


def listar_pacientes(paciente_service):
    pacientes = paciente_service.listar()

    if not pacientes:
        print("Nenhum paciente cadastrado.")
        return

    print("\nPacientes cadastrados:")

    for paciente in pacientes:
        print(f"Nome: {paciente.nome}")
        print(f"Idade: {paciente.idade}")
        print(f"Telefone: {paciente.telefone}")
        print()


def buscar_paciente(paciente_service):
    nome = input("Digite o nome do paciente: ")

    pacientes_encontrados = paciente_service.buscar_por_nome(nome)

    if not pacientes_encontrados:
        print("Nenhum paciente encontrado.")
        return

    print("\nPacientes encontrados:")

    for paciente in pacientes_encontrados:
        print(f"Nome: {paciente.nome}")
        print(f"Idade: {paciente.idade}")
        print(f"Telefone: {paciente.telefone}")
        print()


paciente_service = PacienteService()

while True:
    print("\nClínica Vida+")
    print("1. Cadastrar paciente")
    print("2. Listar pacientes")
    print("3. Buscar paciente")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_paciente(paciente_service)

    elif opcao == "2":
        listar_pacientes(paciente_service)

    elif opcao == "3":
        buscar_paciente(paciente_service)

    elif opcao == "4":
        print("Encerrando o sistema...")
        break

    else:
        print("Opção inválida.")