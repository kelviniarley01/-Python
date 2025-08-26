# Sistema de Cadastro de Pacientes (usando lista)

pacientes = []  # Lista que guarda os pacientes

while True:
    print("\n--- Sistema de Cadastro de Pacientes ---")
    print("1 - Cadastrar o paciente")
    print("2 - Mostrar os pacientes cadastrados")
    print("3 - Atender o paciente")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do paciente: ")
        pacientes.append(nome)  # adiciona na lista
        print(f"paciente {nome} cadastrado com sucesso!")

    elif opcao == "2":
        if len(pacientes) == 0:
            print("Nenhum paciente foi cadastrado.")
        else:
            print("\n Pacientes cadastrados com sucesso:")
            for i, p in enumerate(pacientes, start=1):
                print(f"{i}. {p}")

    elif opcao == "3":
        if len(pacientes) == 0:
            print("Nenhum paciente para ser atendido no momento.")
        else:
            atendido = pacientes.pop(0)  # remove o primeiro da lista
            print(f" Paciente {atendido} foi atendido.")

    elif opcao == "4":
        print(" Saindo do sistema com sucesso...")
        break

    else:
        print("Opção inválida ou Incorreta, tente novamente.")
