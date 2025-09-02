usuarios = []  # lista de usuários

while True:
    print("\n--- Página Inicial ---")
    print("1 - Cadastrar Usuário")
    print("2 - Pesquisar e-mail e mostrar nome")
    print("3 - Fazer login")
    print("4 - Ver todos os usuários cadastrados")
    print("5 - Sair do programa")

    opcao = input("Escolha uma das opções: ")

    if opcao == "1":
        nome = input("Digite o nome: ")
        email = input("Digite o e-mail: ")
        senha = input("Digite a senha: ")
        usuario = {"nome": nome, "email": email, "senha": senha}
        usuarios.append(usuario)
        print("Usuário cadastrado com sucesso!")

    elif opcao == "2":
        email = input("Digite o e-mail para procurar: ")
        achou = False
        for u in usuarios:
            if u["email"] == email:
                print("Esse e-mail pertence a:", u["nome"])
                achou = True
        if not achou:
            print("E-mail não encontrado!")

    elif opcao == "3":
        email = input("Digite o e-mail: ")
        senha = input("Digite a senha: ")
        logado = False
        for u in usuarios:
            if u["email"] == email and u["senha"] == senha:
                print("Login realizado com sucesso! Bem-vindo,", u["nome"])
                logado = True
        if not logado:
            print("E-mail ou senha incorretos!")

    elif opcao == "4":
        if len(usuarios) == 0:
            print("Nenhum usuário cadastrado ainda.")
        else:
            print("\nUsuários cadastrados:")
            for i, u in enumerate(usuarios, start=1):
                print(i, "-", u["nome"], "(", u["email"], ")")

    elif opcao == "5":
        print("Saindo do programa com sucesso!")
        break

    else:
        print("Opção inválida, tente novamente!")
