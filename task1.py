def count_vowels(word):
    return len([char for char in word if char in 'аеёиоуыэюяАОУЫИЭЯЁЮЕ'])

def check_rhythm(poem):
    words = poem.split()
    counts = list(map(count_vowels, words))
    return all(count == counts[0] for count in counts)

poem = input("Введите стихотворение Винни-Пуха: ")
if check_rhythm(poem):
    print("Парам пам-пам")
else:
    print("Пам парам")