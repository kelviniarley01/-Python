from dataclasses import dataclass
from datetime import datetime

@dataclass
class Cliente:
    nome: str
    telefone: str
    email: str
    
@dataclass
class Servico:
    descricao: str
    valor:int
    
@dataclass
class Peca:
    nome: str
    preco_custo: int
    quantidade: int
    
@dataclass
class OrdemServico:
    cliente: Cliente
    servicos: list[Servico]
    pecas: list[Peca]
    status: str
    data_entrega:datetime
    data_saida: datetime
    
# Lista em Memória #
cliente: list[cliente] = []
pecas_estoque: list[Peca] = []
ordens: list[OrdemServico] = []

def cadastrar_clientes():
    nome = input("Qual o Nome do Cliente?")
    telefone = input("Qual número de telefone?")
    email = input("Qual o seu email para entrar em contato?")
    c = cliente(nome, telefone, email)
    clientes.append(c)
    print("Cliente cadastrado com sucesso!")
    
def adicionar_peca():
    nome = input("Qual o nome da Peça?")
    preco = int("Qual o preço da Peça?")
    quantidade = int(input("Quantidade em estoque"))
    pecas_estoque.append(Peca(nome, preco, quantidade))
    print("Peças adicionadas com Sucesso!")
    
def nova_ordem():
    if not clientes:
        print("Cadastre um cliente primeiro.")
        return

    print("Clientes disponíveis:")
    for i, c in enumerate(clientes):
        print(f"{i} - {c.nome}")
    idx = int(input("Escolha o número do cliente: "))
    cliente = clientes[idx]

    servicos = []
    while True:
        desc = input("Descrição do serviço (ENTER para parar): ")
        if not desc:
            break
        valor = int(input("Valor do serviço: "))
        servicos.append(Servico(desc, valor))

    ordem = OrdemServico(cliente, servicos, [], "análise", datetime.now())
    ordens.append(ordem)
    print("Ordem de serviço criada!")


def listar_ordens():
    if not ordens:
        print("Nenhuma ordem cadastrada.")
        return
    for i, o in enumerate(ordens):
        saida = o.data_saida.strftime("%d/%m %H:%M") if o.data_saida else "—"
        print(f"{i} - Cliente: {o.cliente.nome} | Status: {o.status} | Entrada: {o.data_entrada.strftime('%d/%m %H:%M')} | Saída: {saida}")


    
def atualizar_status():
    listar_ordens()
    idx = int(input("Novo status(análise/ orçamento/ aguardando peça/ em manuntenção/testando/pronto"))
    ordens[idx].status = novo
    if not ordens:
        print("Nenhuma ordem.")
        return
    for i, o in enumerate(ordens):
        print("f {i} - Cliente: o{o.clientes.nome} | Status: o{status} | Entrada: {o.data_entrada.strtime(dd/mm/h/m)")

def relatorios():
    print("\n--- Relatório ---")
    print(f"Total de ordens: {len(ordens)}")
    if ordens:
        tempos = [ (o.data_saida - o.data_entrada).total_seconds()/3600
                   for o in ordens if o.data_saida ]
        if tempos:
            media = sum(tempos)/len(tempos)
            print(f"Tempo médio (horas): {media:.1f}")
    print("-----------------\n")

# ---------- Menu ----------
def menu():
    while True:
        print("\n--- TechFix ---")
        print("1 - Cadastrar cliente")
        print("2 - Adicionar peça ao estoque")
        print("3 - Nova ordem de serviço")
        print("4 - Atualizar status de ordem")
        print("5 - Listar ordens")
        print("6 - Relatórios")
        print("0 - Sair")
        op = input("Escolha: ")
        if op == "1": cadastrar_cliente()
        elif op == "2": adicionar_peca()
        elif op == "3": nova_ordem()
        elif op == "4": atualizar_status()
        elif op == "5": listar_ordens()
        elif op == "6": relatorios()
        elif op == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()
