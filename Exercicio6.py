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
        print("Cadastre um cliente primeiro")
        return
    for i, c in enumerate(cliente)
        print(f"{i} - {c.nome}")
    idx = int(input("Escolha o cliente"))
    cliente = clientes[idx]
    
    servicos = []
    while True:
        desc = input("Descrição do Serviço")
        if not desc:
            break
        valor = int(input("Qual o Valor do Seriço?"))
        servicos.append(Servicos(des, valor))
        
    ordem = OrdemServico(cliente, servicos, [], "análise", datetime.now())
    ordens.append(ordem)
    print("Ordem de Serviço Cadastrada!")
    
def atualizar_status():
    listar_ordens()
    idx = int(input("Novo status(análise/ orçamento/ aguardando peça/ em manuntenção/testando/pronto"))
    ordens[idx].status = novo
    if not ordens:
        print("Nenhuma ordem.")
        return
    for i, o in enumerate(ordens):
        print("f")