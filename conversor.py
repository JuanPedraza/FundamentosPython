pesos = float(input("¿Cuántos pesos colombianos tienes?: "))

dollar = 3800

dollars = pesos / dollar

dollars = round(dollars, 2)

print(f'Tienes {dollars} dólares al cambio')