import random


def run():
    number_random = random.randint(1,100)
    number_choice = int(input('Escoge un número del 1 al 100: '))
    while number_choice != number_random:
        if number_choice < number_random:
            print('Busca un número mayor')
        else: 
            print('Busca un número menor')
        number_choice = int(input('Escoge otro número: '))
    print('Excelente, has adivinado')


if __name__ == "__main__":
    run()