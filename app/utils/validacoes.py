import re


def limpar_texto(valor):
    if valor is None:
        return ""

    valor = str(valor).strip()

    valor = valor.replace("<", "")
    valor = valor.replace(">", "")

    return valor


def validar_email(email):
    email = limpar_texto(email)

    padrao = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    return re.match(padrao, email) is not None


def somente_numeros(valor):
    return re.sub(r"\D", "", str(valor or ""))


def validar_cpf(cpf):
    cpf = somente_numeros(cpf)

    if len(cpf) != 11:
        return False

    if cpf == cpf[0] * 11:
        return False

    return True


def validar_inteiro_positivo(valor):
    try:
        return int(valor) > 0
    except Exception:
        return False
