def palindromo(word):
    word = word.replace(' ', '')
    word = word.lower()
    word_invertida = word[::-1]
    if word == word_invertida:
        return True
    else:
        return False

def run():
    word = input('Escribe una palabra: ')
    es_palindromo = palindromo(word)
    if es_palindromo == True:
        print('Es palíndromo')
    else:
        print('No es palíndromo')

if __name__ == '__main__':
    run()

