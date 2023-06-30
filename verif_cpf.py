import sys


# Verificação da localidade do CPF
def ver_sigla(tupla_cpf):
    if tupla_cpf[8] == 1:
        lista_estados = ["DF", "GO", "MS", "MS", "MT", "TO"]
        return lista_estados
    elif tupla_cpf[8] == 2:
        lista_estados = ["AC", "AM", "AP", "PA", "RO", "RR"]
        return lista_estados
    elif tupla_cpf[8] == 3:
        lista_estados = ["CE", "MA", "PI"]
        return lista_estados
    elif tupla_cpf[8] == 4:
        lista_estados = ["AL", "PB", "PE", "RN"]
        return lista_estados
    elif tupla_cpf[8] == 5:
        lista_estados = ["BA", "SE"]
        return lista_estados
    elif tupla_cpf[8] == 6:
        lista_estados = ["MG"]
        return lista_estados
    elif tupla_cpf[8] == 7:
        lista_estados = ["ES", "RJ"]
        return lista_estados
    elif tupla_cpf[8] == 8:
        lista_estados = ["SP"]
        return lista_estados
    elif tupla_cpf[8] == 9:
        lista_estados = ["PR", "SC"]
        return lista_estados
    elif tupla_cpf[8] == 0:
        lista_estados = ["RS"]
        return lista_estados

def calculo1(tupla_cpf):
    calculo_digito = tupla_cpf[:9]
    indice = 0
    multi = 10
    soma1 = 0
    for digito in calculo_digito:
        calculo_digito1 = int(calculo_digito[indice]) * multi
        indice = indice + 1
        multi = multi - 1
        soma1 += calculo_digito1
        if indice == 9:
            return soma1

def digito_verificador1(digito1):
    resto = int(digito1) % 11
    digito1_definitivo = 11 - int(resto)
    return digito1_definitivo


def calculo2(tupla_cpf, digito_v1):
    calculo_digito = tupla_cpf[:9]
    calculo_digito = tupla_cpf[1:]
    lista_temporaria = list(calculo_digito)
    lista_temporaria.append(digito_v1)
    calculo_digito = tuple(lista_temporaria)
    indice = 0
    multi = 10
    soma2 = 0
    for digito in calculo_digito:
        calculo_digito1 = int(calculo_digito[indice]) * multi
        indice = indice + 1
        multi = multi - 1
        soma2 += calculo_digito1
        if indice == 9:
            return soma2

def digito_verificador2(digito2):
    resto = int(digito2) % 11
    digito2_definitivo = 11 - int(resto)
    return digito2_definitivo


# main
while True:
    verificar = input("\nDigite seu CPF para a verificação: ")
    verificar_limitado = verificar[:11]
    if not verificar_limitado.isdigit():
        print("Digite apenas números!")
    else:
        break
tupla_cpf = tuple(int(digito) for digito in verificar_limitado)
localidade = ver_sigla(tupla_cpf)
digito = calculo1(tupla_cpf)
digito_v1 = digito_verificador1(digito)
if int(digito_v1) != tupla_cpf[9]:
    print("Seu CPF não é válido! Consulte a Receita Federal!")
    sys.exit()
else:
    segundo = calculo2(tupla_cpf, digito_v1)
    digito_v2 = digito_verificador2(segundo)
    if int(digito_v2) != tupla_cpf[10]:
        print("Seu CPF não é válido! Consulte a Receita Federal!")
        sys.exit()
    else:
        cpf = str(tupla_cpf)
        print(f"Muito bem! Seu CPF de número {cpf} foi emitido no estado de {localidade} e consta como válido!")