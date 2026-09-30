# Passo 2: Sistema Simplificado em Python - Clínica Vida+
# Aluno: Gabriel Tenorio
# Objetivo: Cadastrar pacientes, calcular estatísticas e gerenciar dados em memória.

# Lista para guardar os dicionários de pacientes
pacientes = []

while True:
    print("\n=== SISTEMA CLÍNICA VIDA+ ===")
    print("1. Cadastrar paciente")
    print("2. Ver estatísticas")
    print("3. Buscar paciente")
    print("4. Listar todos os pacientes")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")

    # --- OPÇÃO 1: CADASTRAR PACIENTE ---
    if opcao == "1":
        try:
            print("\n--- Novo Cadastro ---")
            nome = input("Nome do paciente: ")

            # Tenta converter idade para inteiro. Se falhar, vai para o "except"
            idade = int(input("Idade: "))
            telefone = input("Telefone: ")

            # Cria o dicionário do paciente
            novo_paciente = {
                "nome": nome,
                "idade": idade,
                "telefone": telefone
            }

            # Adiciona à lista principal
            pacientes.append(novo_paciente)
            print(">> Paciente cadastrado com sucesso!")

        except ValueError:
            print(">> Erro: A idade deve ser um número inteiro válido.")

    # --- OPÇÃO 2: VER ESTATÍSTICAS ---
    elif opcao == "2":
        total = len(pacientes)

        if total > 0:
            soma_idades = 0

            # Inicializa as variáveis de comparação com o primeiro paciente da lista
            mais_novo = pacientes[0]
            mais_velho = pacientes[0]

            for p in pacientes:
                # Soma para a média
                soma_idades += p["idade"]

                # Verifica se é o mais novo
                if p["idade"] < mais_novo["idade"]:
                    mais_novo = p

                # Verifica se é o mais velho
                if p["idade"] > mais_velho["idade"]:
                    mais_velho = p

            media = soma_idades / total

            print("\n--- Estatísticas da Clínica ---")
            print(f"Número total de pacientes: {total}")
            print(f"Idade média: {media:.1f} anos")
            print(f"Paciente mais novo: {mais_novo['nome']} ({mais_novo['idade']} anos)")
            print(f"Paciente mais velho: {mais_velho['nome']} ({mais_velho['idade']} anos)")

        else:
            print("\n>> Não há dados suficientes para gerar estatísticas (nenhum paciente cadastrado).")

    # --- OPÇÃO 3: BUSCAR PACIENTE ---
    elif opcao == "3":
        nome_busca = input("\nDigite o nome para buscar: ").lower()
        encontrado = False

        print("\n--- Resultados da Busca ---")

        for p in pacientes:
            # Verifica se o nome digitado está contido no nome do paciente
            if nome_busca in p["nome"].lower():
                print(f"Nome: {p['nome']} | Idade: {p['idade']} | Tel: {p['telefone']}")
                encontrado = True

        if not encontrado:
            print(">> Paciente não encontrado.")

    # --- OPÇÃO 4: LISTAR TODOS ---
    elif opcao == "4":
        print("\n--- Lista Geral de Pacientes ---")

        if len(pacientes) > 0:
            for i, p in enumerate(pacientes, start=1):
                print(f"{i}. Nome: {p['nome']} | Idade: {p['idade']} | Tel: {p['telefone']}")
        else:
            print(">> A lista está vazia.")

    # --- OPÇÃO 5: SAIR ---
    elif opcao == "5":
        print("Saindo do sistema...")
        break

    else:
        print(">> Opção inválida. Tente novamente.")