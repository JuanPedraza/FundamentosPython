def conversor(tipo_pesos, valor_dolar):
    pesos = float(input(f"¿Cuántos pesos {tipo_pesos} tienes?: "))
    dollars = pesos / valor_dolar
    dollars = round(dollars, 2)
    print(f'Tienes {dollars} dólares al cambio')

menu = """
Bienvenido al conversor de monedas

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opción: """

option = int(input(menu))

if option == 1:
    conversor('colombianos', 3800)
elif option == 2: 
    conversor('argentinos', 65)
elif option == 3:
    conversor('mexicanos', 24)
else:
    print('Ingrese una opción válida')
