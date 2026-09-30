from models.paciente import Paciente
from services.paciente_service import PacienteService


paciente_service = PacienteService()

paciente1 = Paciente("João Silva", 45, "(11) 99999-9999")
paciente2 = Paciente("Maria Souza", 30, "(11) 98888-8888")

paciente_service.cadastrar(paciente1)
paciente_service.cadastrar(paciente2)

for paciente in paciente_service.listar():
    print(f"Nome: {paciente.nome}")
    print(f"Idade: {paciente.idade}")
    print(f"Telefone: {paciente.telefone}")
    print()

resultado = paciente_service.buscar_por_nome("sou")

print("Resultado da busca:")

for paciente in resultado:
    print(f"Nome: {paciente.nome}")
    print(f"Idade: {paciente.idade}")
    print(f"Telefone: {paciente.telefone}")