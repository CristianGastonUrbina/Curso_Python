# hipoteca.py
# Archivo de ejemplo
# Ejercicio de hipoteca
saldo = 500000
pagoMensual = 2684.11
tasa = 0.05
años = 30
totalPagado = 0
meses = 0
adelanto = 1000
pagoExtraMesFin = 108
pagoExtraMesComienzo = 61


while saldo>0 :
    meses += 1
    if (meses >= pagoExtraMesComienzo) and (meses<=pagoExtraMesFin):
        if saldo < pagoMensual + adelanto:
            totalPagado = totalPagado + saldo
            saldo = 0
        else:
            saldo = saldo * (1+tasa/12) - pagoMensual - adelanto
            totalPagado = totalPagado + pagoMensual + adelanto
    else :
        if saldo < pagoMensual:
            totalPagado = totalPagado + saldo
            saldo = 0
        else:
            saldo = saldo * (1+tasa/12) - pagoMensual
            totalPagado += + pagoMensual
    f = f"El mes {meses} se pago {round(totalPagado,2)} y el saldo restante es de {round(saldo,2)}"
    print (f)

print( "Total Pagado ", round(totalPagado,2), "en ",meses, " meses")