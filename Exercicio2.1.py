oficina = []  # Lista que guarda os carros

while True:
    print("\n--- Sistema de Oficina ---")
    print("1 - Cadastrar Carro e qual o problema")
    print("2 - Mostrar Carros Cadastrados")
    print("3 - Atender carro")
    print("4 - Data para Entrega")
    print("5 - Sair")

    opcao = input("Escolha uma das opções: ")

    if opcao == "1":
        nome = input("Digite o nome do carro e qual o problema: ")
        oficina.append(nome)  # adicionar na lista
        print(f"Oficina: {nome} cadastrado com sucesso!")

    elif opcao == "2":
        if len(oficina) == 0:
            print("Nenhum carro foi cadastrado no momento.")
        else:
            print("\nCarros cadastrados: ")
            for i, p in enumerate(oficina, start=1):
                print(f"{i}. {p}")

    elif opcao == "3":
        if len(oficina) == 0:
            print("Nenhum carro para atender no momento.")
        else:
            atendido = oficina.pop(0)  # remove o primeiro da lista
            print(f"Problema do carro {atendido} foi atendido.")

    elif opcao == "4":
        print("Data para entrega do veículo: ")
        data = input("Digite a data da entrega (dd/mm/aaaa): ")
        print(f"Data de entrega registrada: {data}")

    elif opcao == "5":
        print("Saindo do sistema com sucesso!")
        break

    else:
        print("Opção inválida. Tente novamente.")
