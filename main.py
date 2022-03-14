from banco import Banco
from cliente import Cliente
from conta import ContaCorrente, ContaPoupanca
from funcoes import *
from random import randint

print('SEJA BEM-VINDE AO BANCO SENNA')
print('O banco que nem parece banco, porque não é mesmo...')
print()

banco_senna = Banco()
cliente = ''
nome = ''
conta = ''
senha_conta = 0

while True:
    print('O que deseja fazer? ')
    print()
    print('[1] Acessar conta.')
    print('[2] Sacar.')
    print('[3] Depositar.')
    print('[4] Criar conta')
    print('[5] Sair.')
    print()
    comando = input('>>')

    while not check(comando):
        print('Ação inválida, digite um número válido: ')
        comando = input('>>')

    if comando == '1':
        print('Digite o seu nome:')
        nome_temp = input('>>')
        while not nome_check(nome_temp):
            print('Digite apenas letras:')
            nome_temp = input('>>')

        if nome_temp == cliente:
            print('Digite a sua senha:')
            senha = input('>>')
            if senha == senha_conta:
                nome.inserir_conta(conta)
                banco_senna.inserir_cliente(nome)
                banco_senna.inserir_conta(conta)
                print('Acesso completo.')

            else:
                print('Senha inválida.')

        else:
            print('Conta não existe, porfavor crie a sua conta.')

    elif comando == '2':
        print('Quanto deseja sacar?')
        sac = input('>>')
        while not val_check(sac):
            print('Valor inválido, digite apenas números:')
            sac = input('>>')

        if banco_senna.autenticar(nome):
            conta.sacar(sac)
        else:
            print('Usuário não autenticado, porfavor acesse a sua conta.')
            print()

    elif comando == '3':
        print('Quanto deseja depositar?')
        dep = input('>>')
        while not val_check(dep):
            print('Valor inválido, digite apenas números:')
            dep = input('>>')

        if banco_senna.autenticar(nome):
            conta.depositar(dep)
        else:
            print('Usuário não autenticado, porfavor acesse a sua conta.')
            print()

    elif comando == '4':
        print('Digite o seu nome:')
        nome = input('>>')
        while not nome_check(nome):
            print('Digite apenas letras:')
            nome = input('>>')
        print()

        print('Digite a sua idade:')
        idade = input('>>')
        while not idade_check(idade):
            print('Idade inválida, digite apenas números:')
            idade = input('>>')
        print()

        print('Muito bom agora digite o seu CPF:')
        cpf = input('>>')
        while not cpf_check(cpf):
            print(f'{cpf} é um CPF inválido, por favor digite apenas números')
            cpf = input('>>')
        print()

        senha_conta = 0
        senha_2 = 1

        while not senha_conta == senha_2:
            print('Crie uma senha:')
            senha_conta = input('>>')

            print('Confirme a sua senha:')
            senha_2 = input('>>')

            if senha_conta == senha_2:
                continue
            else:
                print('Senhas não coincidem')
                continue

        print('Ok, tudo correto.')
        print('Gostaria de criar uma Conta-corrente, ou uma Conta-poupança?')
        print('[cc] Conta-corrente')
        print('[cp] Conta-corrente')
        ct = input('>>')
        while not ct_check(ct):
            print('Opção inválida, digite [cc] ou [cp]:')
            ct = input('>>')

        if ct == 'cc':
            cliente = nome
            nome = Cliente(nome, idade)

            if randint(1, 3) == 1:
                ag = 1030
            elif randint(1, 3) == 2:
                ag = 1443
            else:
                ag = 2399

            print('Gostaria de depositar um valor inicial?')
            val = input('>>')
            while not val_check(val):
                print('Valor inválido, digite apenas números:')
                val = input('>>')

            conta = ContaCorrente(ag, randint(11111, 99999), saldo=float(val))

            print('Conta criada com sucesso.')
            conta.detalhar()

        else:
            cliente = nome
            nome = Cliente(nome, idade)

            if randint(1, 3) == 1:
                ag = 1030
            elif randint(1, 3) == 2:
                ag = 1443
            else:
                ag = 2399

            print('Gostaria de depositar um valor inicial?')
            val = input('>>')
            while not val_check(val):
                print('Valor inválido, digite apenas números:')
                val = input('>>')

            conta = ContaPoupanca(ag, randint(11111, 99999), saldo=float(val))

            print('Conta criada com sucesso.')
            conta.detalhar()

    elif comando == '5':
        break

    else:
        pass
