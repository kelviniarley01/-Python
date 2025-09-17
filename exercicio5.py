from dataclasses import dataclass
from datetime import datetime

@dataclass
class corte:
    corte_simples: 25
    corte_e_barba: 35
    barba_completa: 20
    corte_social: 30

class pessoa:
    nome: str
    telefone: str
    email: str

class barbeiro:
    nome: str
    telefone: str
    horario: str
        
listaA = [] 
listaB = []
def agendar():
    nome = input("Qual o seu nome: ")
    email = input("Qual o seu email: ")
    telefone = input("Qual o seu número: ")
    agendamento_digitado = pessoa(nome,email,telefone)
    listaA.append(agendamento_digitado)
    print("Agendamento efetuado com sucesso")
    
def agenda_do_barbeiro():
    nome = input ("Quem vai ser o Barbeiro? ")
    telefone = input("Qual o telefone do Barbeiro?")
    horario = input("Qual o horario desejado?")
    agenda_digitado = agenda(nome, telefone, horario)
    listaB.append(agenda_digitado)
    print("Cadastro de Agenda do Barbeiro feito com sucesso")
    
def servicos():
    tipo_de_corte = input ("Qual o tipo do seu corte?")
    tempo = input ("Quanto tempo deve ser feito o corte?")
    preco = input ("O preço do corte é:")
    
def pagamento():
    tipo_de_pagamento = input ("Qual vai ser a Forma de Pagamento?")
    pagamento = input ("O pagamento ai ser em Dinheiro, Cartão ou PIX ?")
    dinheiro = input("Insira o Valor do Pagamento em dinheiro:")
    cartão = input("O cartão é da Visa ou da MasterCard?")
    PIX = input ("Qual a chave pix para o pagamennto?")
    return ("A chave PIX é 13996534567")
    pagamento_digitado = pagamento(dinheiro, cartão, PIX)
    listaA.append(pagamento_digitado)
    print("Pagamento Feito com Sucesso")
    
def contato():
    contato = input("Escolha a forma de Contato:")
    telefone = input("O telefone é 13 99653-4567")
    email = input ("O email é xxxxxxxxxxxxx@gmail.com")
    contato_digitado = contato(telefone, email)
    listaB.append(contato_digitado)
    print("Entraremos em Contato")
    
def cancelar_servico():
    cancelar_corte = input("Deseja cancelar o seu corte?")
    corte_cancelado = input("Seu corte foi cancelado")
    nao_cancelar = input("Seu corte não foi cancelado")
    cancelamento_corte = cancelar_corte(corte_cancelado, nao_cancelar)
    listaA.append(cancelamento_corte)
    
def remarcar():
    remarcar_corte =  input("Deseja remarcar seu corte?")
    remarque_dia = input("Deseja remarcar em qual dia?")
    remarque_hr = input("Em qual horario voce deseja cortar?")
    remarque_agen = input("Seu servico foi remarcado!")
    remarque_corte = remarque_agen(remarcar_corte, remarque_dia, remarque_hr)
    listaA.append(remarque_corte)
    
def fazer_login():
    login_email = input("Qual o seu email: ")
    login_senha = input("Qual a sua senha: ")
        
    for usuario in lista_usuarios:
        if usuario.email == login_email and usuario.senha == login_senha:
            print("Acesso autorizado")
            return usuario
            
def fazer_cadastro():
    cadastro_email = input("Qual o seu email: ")
    cadastro_senha = input("Qual a sua senha: ")
    cadastro_nome = input("Qual o seu nome?")
        
    for usuario in listaB:
        if usuario.email == cadastro_email and usuario.senha == cadastro_senha:
            print("Cadastro feito!")
            return usuario 
    
def mostrar_menu():
    print("\n ===Bem Vindo a Barbearia! O que Deseja fazer?")
    print("1 -Agendar")
    print("2- Cadastrar Agenda do Barbeiro")
    print("3- Cadastro de Serviço")
    print("4- Qual a forma de pagamento?")
    print("5 - formas de Contato")
    print("6 - Cancelamento")
    print("7 - Remarcar")
    print("8 - Fazer Login Ou Cadastro")
    print("0 - Sair")
    
    
    usuario_atual = None
    
    while True:
        opcao = mostra_menu()
        
        if opcao == "1":
            agendar_corte()
            
        elif opcao == "2":
            cadastrar_agenda()
            
        elif opcao == "3":
            cadastrar_servico()
            
        elif opcao =="4":
            forma_de_pagamento()
            
        elif opcao =="5":
            formas_de_contato()
            
        elif opcao =="6":
            cancelar_servico()
            
        elif opcao =="7":
            remarcar_servico()
            
        elif opcao =="8":
            log_cadastro()
            
        elif opcao =="0":
            print("Saindo...")
            break
        
        else:
            print("Opção invalida, tente novamente!")
            
        