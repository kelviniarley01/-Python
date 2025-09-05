usuarios = []  # Lista para guardar as publicações

while True:
    print("\n--- Página Inicial ---")
    print("1 - Criar Publicação")
    print("2 - Curtir Publicação")
    print("3 - Visualizar Feed")
    print("4 - Visualizar Publicação")
    print("5 - Sair")
    
    opcao = input("Escolha uma das opções: ")

    if opcao == "1":
        texto = input("Qual o conteúdo da publicação? ")
        descrever = input("Descreva a publicação: ")
        autor = input("Autor: ")
        data = input("Digite a data da publicação (dd/mm/aaaa hh:mm): ")

        # Cada publicação é um dicionário
        publicacao = {
            "texto": texto,
            "descricao": descrever,
            "autor": autor,
            "data": data,
            "curtidas": 0
        }

        usuarios.append(publicacao)
        print("Publicação divulgada com sucesso!")

    elif opcao == "2":
        if len(usuarios) == 0:
            print("Ainda não existem publicações.")
        else:
            for i, pub in enumerate(usuarios):
                print(f"{i+1} - {pub['texto']} (Curtidas: {pub['curtidas']})")
            escolha = int(input("Qual publicação deseja curtir? "))
            if 1 <= escolha <= len(usuarios):
                usuarios[escolha-1]["curtidas"] += 1
                print("Você curtiu a publicação!")
            else:
                print("Opção inválida.")

    elif opcao == "3":
        if len(usuarios) == 0:
            print("Nenhuma publicação no feed.")
        else:
            print("\n--- FEED ---")
            for i, pub in enumerate(usuarios):
                print(f"{i+1} - {pub['texto']} | Autor: {pub['autor']} | Curtidas: {pub['curtidas']}")

    elif opcao == "4":
        if len(usuarios) == 0:
            print("Nenhuma publicação para visualizar.")
        else:
            for i, pub in enumerate(usuarios):
                print(f"{i+1} - {pub['texto']}")
            escolha = int(input("Digite o número da publicação: "))
            if 1 <= escolha <= len(usuarios):
                pub = usuarios[escolha-1]
                print("\n--- DETALHES DA PUBLICAÇÃO ---")
                print("Texto:", pub["texto"])
                print("Descrição:", pub["descricao"])
                print("Autor:", pub["autor"])
                print("Data:", pub["data"])
                print("Curtidas:", pub["curtidas"])
            else:
                print("Opção inválida.")

    elif opcao == "5":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida, tente novamente.")

