tv=["Следствие вели с Леонидом Каневским","Новости","Прогноз погоды","Пусть говорят"]
for tele in tv:
    print(tele)
jija=input("Введите передачу")
x=int(input("Введите позицию в списке"))
tv.insert(x,jija)
for tele in tv:
    print(tele)