def saque(valor):
    limiteDeCredito = 15
    saldo = 10
    status = False
    if valor <= saldo:
        saldo = saldo - valor
        status = True
    else:
        if valor <= limiteDeCredito:
            limiteDeCredito = limiteDeCredito - valor
            status = True

    print(saldo)
    print(limiteDeCredito)
    print(status)

saque(1)

