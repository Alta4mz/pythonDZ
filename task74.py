color=['Красный','Синий','Зеленый','Желтый','Черный','Белый','Фиолетовый','Розовый','Цвет морской волны','Серый']
x=int(input("Выберите число от 0 до 4"))
y=int(input("Выберите число от 5 до 9"))
del color[y:9]
del color[0:x]

print(color)