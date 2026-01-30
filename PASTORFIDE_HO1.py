

word = input("Enter a word: ")
lenght = len(word)

t = 0
lista = []

for i in range (1, lenght+1, 1):
    number = int(input("Enter a number: "))
    lista.append(number)
    t += number
print(lista)
print(f"The lenght of the word is {lenght}")
print(f"The average is {t/lenght}")

if lenght > t:
    print(f'The lenght of the word "{word}" is greater than average ')
elif lenght < t:
    print(f'The lenght of the word "{word}" is less than the average ')
else:
    print(f'The lenght of the word "{word}" is equal the average')

