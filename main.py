#люба строка це список де кожен елемент це символ із строки

word = 'Fotball,volleyball,skate'
#print(len(word))            #індекси починаються від 0
#print(word.count('t'))
#print(word.upper())          #upper робить всі букви більшими
#print(word.isupper())        #isupper дає true або false чи є букви великими
#print(word.lower())          #lower робить всі маленькими
#print(word.islower())        #islower дає true або false чи є букви маленькими
#print(word.capitalize())     #capitilize приводить каждий перший символ любого слова до великої букви (верхний регістр)
#print(word.find('p'))        #find виводить індекс(знаходження) символа
#print(word.split(','))       #split розбиває слова по колонкам (робить список)

hobby = word.split(",")
print(hobby[1])

for i in range(len(hobby)):                #создаємо диапазон в якому до длінни всього списку у нас буде йти цикл
    hobby[i] = hobby[i].capitalize()
print(hobby)

result = ", ".join(hobby)                 #join метод соиденения, передача обичної строки
print(result)

k = 'Football'
#Срези - обращение к нескольким индексам
print(k[0:4])                       # [стартовий елемент : конечний елемент]
print(k[4:])                        # [від 4 до кінця]
print(k[1:7:2])                     # [від якого:до яокго:шаг]


list = [6, 2, "list", True, 7.2]
print(list[2:5:1])
print(list[::-1])                 # якщо вказати в кінці то список перевернеться
