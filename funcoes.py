def check(valor):
    if valor.isnumeric():
        if 0 < int(valor) < 6:
            return True
    else:
        return False


def nome_check(valor):
    if isinstance(valor, str):
        return True
    else:
        return False


def idade_check(valor):
    if valor.isnumeric():
        if int(valor) >= 18:
            return True
        else:
            return False
    else:
        return False


def cpf_check(cpf):
    n_cpf = len(cpf)

    while not cpf.isnumeric() or not n_cpf == 11:
        print(f'{cpf} é um CPF inválido, por favor digite apenas números')
        cpf = input('>>')
        n_cpf = len(cpf)

    temp_cpf = cpf[:9]
    contador = 10
    total = 0

    for index in range(19):
        if index > 8:
            index -= 9
        total += (int(temp_cpf[index]) * contador)
        contador -= 1

        if contador < 2:
            contador = 11
            dig = 11 - (total % 11)
            if dig > 9:
                dig = 0
            total = 0
            temp_cpf += str(dig)

    sequencia = temp_cpf == str(temp_cpf[0]) * len(cpf)
    if cpf == temp_cpf and not sequencia:
        return True
    else:
        return False


def ct_check(valor):
    if valor == 'cc':
        return True
    elif valor == 'cp':
        return True
    else:
        return False


def val_check(valor):
    if isinstance(float(valor), float):
        if float(valor) > 0:
            return True
    else:
        return False