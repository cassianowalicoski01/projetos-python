import os

clientes_banco = {}


def menu_inicio():
    os.system('cls') or None
    while True:
        estilo_menus("      ( 1 ) CADASTRAR   ( 2 ) ACESSAR CONTA   ( 3 ) FINALIZAR      ")
        opcao_selecionada = int(input("O QUE DESEJA FAZER? \n>> "))
        while opcao_selecionada < 0 or opcao_selecionada > 3:
            opcao_selecionada = int(input("\nATENÇÃO! DIGITE UMA OPÇÃO VÁLIDA: \n>> "))
        if opcao_selecionada == 3:
            os.system('cls') or None
            print("\nPROGRAMA FINALIZADO.\n")
            break
        else:
            acao_inicio(opcao_selecionada)
            break


def acao_inicio(opcao):
    os.system('cls') or None
    match opcao:
        case 1:
            cadastrarCliente()
        case 2:
            acessarConta()


def menu_cliente(nome, cpf):
    os.system('cls') or None
    estilo_menus(f"CONTA DE {nome.upper()}")
    while True:
        estilo_menus("      ( 1 ) SACAR   ( 2 ) DEPOSITAR   ( 3 ) EXTRATO   ( 4 ) EXCLUIR CONTA   ( 5 ) SAIR      ")
        opcao_cliente = int(input("O QUE DESEJA FAZER? \n>> "))
        while opcao_cliente < 0 or opcao_cliente > 5:
            opcao_cliente = int(input("\nATENÇÃO! DIGITE UMA OPÇÃO VÁLIDA: \n>> "))
        if opcao_cliente == 5:
            menu_inicio()
            break
        else:
            acao_cliente(opcao_cliente, nome, cpf)
            break


def acao_cliente(acao, nome_cliente, cpf):
    os.system('cls') or None
    match acao:
        case 1:
            sacar(nome_cliente, cpf)
        case 2:
            depositar(nome_cliente, cpf)
        case 3:
            extrato(nome_cliente, cpf)
        case 4:
            excluirConta(nome_cliente, cpf)


def cadastrarCliente():
    situacao = False
    estilo_menus("CRIE SUA CONTA")
    print()
    nome_cliente = str(input("- DIGITE SEU NOME: ")).capitalize()
    dados_cliente = {}
    dados_cliente["cpf"] = int(input("- DIGITE SEU CPF: "))
    for cliente, valor in list(clientes_banco.items()):
        if cliente == nome_cliente and valor["cpf"] == dados_cliente["cpf"]:
            situacao = True
    if situacao == True:
        print("\nUSUÁRIO JÁ CADASTRADO!\n")
        input("PRESSIONE [ENTER] PARA CONTINUAR...\n\n")
        menu_inicio()
    else:
        dados_cliente["senha"] = str(input("- CRIE UMA SENHA: "))
        dados_cliente["saldo"] = 0
        dados_cliente["num_saques"] = 0
        dados_cliente["num_depositos"] = 0
        clientes_banco[f"{nome_cliente}"] = dados_cliente
        print(f"\nCLIENTE {nome_cliente.upper()} CADASTRADO(A) COM SUCESSO!\n")
        input("PRESSIONE [ENTER] PARA CONTINUAR...\n\n")
        menu_inicio()


def acessarConta():
    situacao = False
    estilo_menus("ACESSAR CONTA")
    print()
    acesso_nome = str(input("- NOME: ")).capitalize()
    acesso_cpf = int(input("- CPF: "))
    acesso_senha = str(input("- SENHA: "))
    for chave, valor in list(clientes_banco.items()):
        if chave == acesso_nome:
            if valor["cpf"] == acesso_cpf and valor["senha"] == acesso_senha:
                situacao = True
    if situacao == True:
        print("\nLOGIN REALIZADO COM SUCESSO!\n")
        input("PRESSIONE [ENTER] PARA CONTINUAR...\n\n")
        menu_cliente(acesso_nome, acesso_cpf)
    else:
        print("\nCPF E/OU SENHA INVÁLIDO(S)\n")
        input("PRESSIONE [ENTER] PARA CONTINUAR...\n\n")
        menu_inicio()


def sacar(nome_cliente, cpf):
    os.system('cls') or None
    print(f"> Conta de {nome_cliente}")
    estilo_menus("SACAR")
    for chave, valor in list(clientes_banco.items()):
        if chave == nome_cliente:
            if valor["cpf"] == cpf:
                print(f"\nSEU SALDO: R${valor["saldo"]:.2f}\n")
                if valor["saldo"] < 1:
                    print(f"{nome_cliente.upper()}, VOCÊ NÃO POSSUI NENHUM SALDO PARA SAQUE!\n")
                    opc_deposito = str(input("GOSTARIA DE FAZER UM DEPÓSITO AGORA MESMO? (S/N): ")).upper()[0]
                    while opc_deposito != "S" and opc_deposito != "N":
                        opc_deposito = str(input(f"\n{nome_cliente.upper()}, RESPONDA APENAS S OU N: ")).upper()[0]
                    if opc_deposito == "S":
                        depositar(nome_cliente, cpf)
                    else:
                        menu_cliente(nome_cliente, cpf)
                else:
                    saque = float(input("VALOR DO SAQUE: R$"))
                    while saque < 1:
                        print("\nATENÇÃO! VALOR MÍNIMO DE R$1,00 PARA SAQUES.")
                        saque = float(input("\nDIGITE UMA VALOR MAIOR PARA O SAQUE: R$"))
                    while saque > valor["saldo"]:
                        print("\nATENÇÃO! VALOR DO SAQUE SUPERIOR AO SEU SALDO.")
                        saque = float(input("\nDIGITE UMA VALOR DISPONíVEL PARA O SAQUE: R$"))
                    valor["saldo"] -= saque
                    valor["num_saques"] += 1
                    print("\nSAQUE CONCLUÍDO COM SUCESSO!")
                    print(f"\nSALDO ATUALIZADO: R${valor["saldo"]:.2f}\n")
                    input("PRESSIONE [ENTER] PARA CONTINUAR...\n\n")
                    menu_cliente(nome_cliente, cpf)


def depositar(nome_cliente, cpf):
    os.system('cls') or None
    print(f"> Conta de {nome_cliente}")
    estilo_menus("DEPOSITAR")
    for chave, valor in list(clientes_banco.items()):
        if chave == nome_cliente:
            if valor["cpf"] == cpf:
                print(f"\nSALDO ATUAL: R${valor["saldo"]:.2f}\n")
                deposito = float(input("VALOR DO DEPÓSITO: R$"))
                while deposito < 1:
                    print("\nATENÇÃO! VALOR MÍNIMO DE R$1,00 PARA DEPOSITOS.\n")
                    deposito = float(input("DIGITE UMA VALOR VÁLIDO PARA DEPÓSITO: R$"))
                valor["saldo"] += deposito
                valor["num_depositos"] += 1
                print("\nDEPÓSITO REALIZADO COM SUCESSO!")
                print(f"\nSALDO ATUALIZADO: R${valor["saldo"]:.2f}\n")
                input("PRESSIONE [ENTER] PARA CONTINUAR...\n\n")
                menu_cliente(nome_cliente, cpf)


def extrato(nome_cliente, cpf):
    print(f"> Conta de {nome_cliente}")
    estilo_menus("EXTRATO")
    for chave, valor in list(clientes_banco.items()):
        if chave == nome_cliente:
            if valor["cpf"] == cpf:
                if valor["num_depositos"] == 0:
                    print("\nVOCÊ AINDA NÃO REALIZOU NENHUMA TRANSAÇÃO.\n")
                    input("PRESSIONE [ENTER] PARA CONTINUAR...\n\n")
                    menu_cliente(nome_cliente, cpf)
                else:
                    print(f"\nSEU SALDO É DE R${valor["saldo"]:.2f}")
                    print(f"QUANTIDADE DE SAQUES REALIZADOS: {valor["num_saques"]}")
                    print(f"QUANTIDADE DE DEPÓSITOS REALIZADOS: {valor["num_depositos"]}")
                    input("\nPRESSIONE [ENTER] PARA CONTINUAR...\n\n")
                    menu_cliente(nome_cliente, cpf)


def excluirConta(nome_cliente, cpf):
    print(f"> Conta de {nome_cliente}")
    estilo_menus("EXCLUIR CONTA")
    for chave, valor in list(clientes_banco.items()):
        if chave == nome_cliente:
            if valor["cpf"] == cpf:
                excluir_conta = str(input(f"{nome_cliente.upper()}, REALMENTE DESEJA EXCLUIR SUA CONTA? (S/N): ")).upper()[0]
                while excluir_conta != "S" and excluir_conta != "N":
                    excluir_conta = str(input(f"\n{nome_cliente.upper()}, RESPONDA APENAS S OU N: ")).upper()[0]
                if excluir_conta == "S":
                    del (clientes_banco[f"{chave}"])
                    print("\nCONTA EXCLUIDA COM SUCESSO!\n")
                    input("PRESSIONE [ENTER] PARA CONTINUAR...\n\n")
                    menu_inicio()
                else:
                    print("\nOPERAÇÃO CANCELADA PELO USUÁRIO.\n")
                    input("PRESSIONE [ENTER] PARA CONTINUAR...\n\n")
                    menu_cliente(nome_cliente, cpf)


def estilo_menus(palavra):
    print("-" * (len(palavra) + 6))
    print(f"*  {palavra}  *")
    print("-" * (len(palavra) + 6))


menu_inicio()