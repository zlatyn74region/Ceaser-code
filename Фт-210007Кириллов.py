#  Берет на ввод у пользователя число, если 
#  оно прошло все проверки на ошибки, то возвращает его.
def input_int(text):
    while True:
        try:
            num = int(input(text))
        except:
            print('Ошибка: нужно ввести число!')
            continue
        return num

# Генерирует алфавит от начального символа до последнего и возвращает его (first_char и end_char).
def get_alphabet(first_char, end_char):
    return [chr(char) for char in range(ord(first_char), ord(end_char) + 1)]

# Использует сдвиг в нашей строке.
def get_char_with_shift(char, shift, alphabet : list):
    return alphabet[(alphabet.index(char) + shift) % len(alphabet)] 

# Создание списка алфавитов.
alphabets = [
                get_alphabet('a', 'z'), 
                get_alphabet('A', 'Z'), 
                get_alphabet('а', 'я'), 
                get_alphabet('А', 'Я')
            ]

# Берем данные у пользователя.
text = input('Введите строку: ')
shift = input_int('Введите сдвиг: ')

done_text = []
is_add = False

# Применение каждому символу строки сдвиг и добавление их в конечный список.
# Если символа нет ни в одном из алфавитов, то к нему сдвиг не применяется, 
# и он добавляется в список.
for char in text:
    is_add = False
    for alphabet in alphabets:
        if char in alphabet:
            done_text.append(get_char_with_shift(char, shift, alphabet))
            is_add = True
    
    if not is_add:
        done_text.append(char)

# Вывод результата.
print('Строка со сдвигом:', ''.join(done_text))