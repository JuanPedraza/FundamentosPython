menu = """
Bienvenido al conversor de monedas

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opción: """

option = int(input(menu))

if option == 1:
    pesos = float(input("¿Cuántos pesos colombianos tienes?: "))
    dollar = 3800
    dollars = pesos / dollar
    dollars = round(dollars, 2)
    print(f'Tienes {dollars} dólares al cambio')
elif option == 2:
    pesos = float(input("¿Cuántos pesos argenitos tienes?: "))
    dollar = 65
    dollars = pesos / dollar
    dollars = round(dollars, 2)
    print(f'Tienes {dollars} dólares al cambio')
elif option == 3:
    pesos = float(input("¿Cuántos pesos mexicanos tienes?: "))
    dollar = 24
    dollars = pesos / dollar
    dollars = round(dollars, 2)
    print(f'Tienes {dollars} dólares al cambio')
else:
    print('Ingrese una opción válida')
