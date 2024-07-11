import os
import random

pacientes = []


def mostrarMenu():
    os.system('cls') or None
    opcao_selecionada = 0
    estiloMenu("( 1 ) CADASTRAR   ( 2 ) LISTAR APLICAÇÕES   ( 3 ) CONSULTAR POR CPF   ( 4 ) EXCLUIR CADASTRO   ( 5 ) SAIR")
    while opcao_selecionada != 5:
        opcao_selecionada = int(input("O QUE DESEJA FAZER?\n➜ "))
        while opcao_selecionada < 1 or opcao_selecionada > 5:
           opcao_selecionada = int(input("ATENÇÃO! DIGITE UMA OPÇÃO VÁLIDA: "))
        acaoEscolhida(opcao_selecionada)
        break
    os.system('cls') or None
    print("PROGRAMA FINALIZADO.")


def acaoEscolhida(num_acao):
    os.system('cls') or None
    match num_acao:
        case 1:
            cadastrarVacina()
        case 2:
            listarAplicacoes()
        case 3:
            consultarCpf()
        case 4:
            excluirCadastro()


def cadastrarVacina():
    estiloMenu("CADASTRAR NOVA VACINA")
    if len(pacientes) < 50:
        lote = [1918, 2344, 1010, 9087, 2666, 2862]
        dados_paciente = {}
        dados_paciente["codigo"] = len(pacientes) + 1
        dados_paciente["nome"] = str(input("\n- NOME PACIENTE: ")).capitalize()
        dados_paciente["cpf"] = int(input("- CPF PACIENTE: "))
        dados_paciente["vacina_aplicada"] = str(input("- VACINA APLICADA: ")).capitalize()
        dados_paciente["lote"] = random.choice(lote)
        pacientes.append(dados_paciente)
        print(f"\nPACIENTE {dados_paciente["nome"].upper()} CADASTRADO COM SUCESS0.\n")
        input("PRESSIONE [ENTER] PARA CONTINUAR...\n\n")
        mostrarMenu()
    else:
        print("\nNÚMERO MAXIMO DE PACIENTES CADASTRADOS.\n")
        input("PRESSIONE [ENTER] PARA CONTINUAR...\n\n")
        mostrarMenu()


def listarAplicacoes():
    if len(pacientes) > 0:
        for paciente in pacientes:
            print()
            estiloMenu(f"DADOS PACIENTE {paciente["nome"].upper()}")
            for chave, valor in paciente.items():
                print(f"{chave.upper().replace("_", " ")}: {valor}")
        input("\n\nPRESSIONE [ENTER] PARA CONTINUAR...\n\n")
        mostrarMenu()
    else:
        print("\nNENHUM PACIENTE CADASTRADO.\n")
        input("PRESSIONE [ENTER] PARA CONTINUAR...\n\n")
        mostrarMenu()


def consultarCpf():
    if len(pacientes) > 0:
        situacao = False
        buscar_cpf = int(input("DIGITE O CPF QUE DESEJA BUSCAR: "))
        while buscar_cpf < 1 or buscar_cpf > 99999999999:
            buscar_cpf = int(input("ATENÇÃO! DIGITE UM CPF VÁLIDO: "))
        for paciente in pacientes:
            for chave, valor in paciente.items():
                if chave == "cpf":
                    if valor == buscar_cpf:
                        situacao = True
                        estiloMenu(f"DADOS PACIENTE {paciente["nome"].upper()}")
                        for chave, valor in paciente.items():
                            print(f"{chave.upper().replace("_", " ")}: {valor}")
                        input("\nPRESSIONE [ENTER] PARA CONTINUAR...\n\n")
                        mostrarMenu()
        if situacao == False:
            print("\nNENHUM PACIENTE CADASTRADO COM O CPF INFORMADO.")
            input("\nPRESSIONE [ENTER] PARA CONTINUAR...\n\n")
            mostrarMenu()
    else:
        print("NENHUM PACIENTE CADASTRADO.")
        input("\nPRESSIONE [ENTER] PARA CONTINUAR...\n\n")
        mostrarMenu()


def excluirCadastro():
    if len(pacientes) > 0:
        situacao = False
        buscar_cpf = int(input("DIGITE O CPF QUE DESEJA EXCLUIR O CADASTRO: "))
        while buscar_cpf < 1 or buscar_cpf > 99999999999:
            buscar_cpf = int(input("ATENÇÃO! DIGITE UM CPF VÁLIDO: "))
        for paciente in pacientes:
            for chave, valor in paciente.items():
                if chave == "cpf":
                    if valor == buscar_cpf:
                        situacao = True
                        excluir_cadastro = str(input(f"\nTEM CERTEZA QUE DESEJA EXCLUIR O CADASTRO DE {paciente["nome"].upper()}? (S/N): ")).upper()[0]
                        while excluir_cadastro != "S" and excluir_cadastro != "N":
                            excluir_cadastro = str(input(f'\nATENÇÃO! DIGITE APENAS "S" OU "N": ')).upper()[0]
                        if excluir_cadastro == "S":
                            pacientes.remove(paciente)
                            print(f"\nCADASTRO DE {paciente["nome"].upper()} EXCLUIDO COM SUCESSO.")
                            input("\nPRESSIONE [ENTER] PARA CONTINUAR...\n\n")
                            mostrarMenu()
                        else:
                            print("\nEXCLUSÃO DO CADASTRO CANCELADA.")
                            input("\nPRESSIONE [ENTER] PARA CONTINUAR...\n\n")
                            mostrarMenu()
        if situacao == False:
            print("\nNENHUM PACIENTE CADASTRADO COM O CPF INFORMADO.")
            input("\nPRESSIONE [ENTER] PARA CONTINUAR...\n\n")
            mostrarMenu()
    else:
        print("NENHUM PACIENTE CADASTRADO.")
        input("\nPRESSIONE [ENTER] PARA CONTINUAR...\n\n")
        mostrarMenu()


def estiloMenu(texto):
    print("▬" * (len(texto) + 8))
    print(f"*   {texto}   *")
    print("▬" * (len(texto) + 8))


mostrarMenu()
