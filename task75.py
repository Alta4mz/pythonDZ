numb=[123,234,345,456]
for numbers in numb:
    print(numbers)
a=int(input("Введите трехзначное число"))
if a==numb[0]:
    print(1)
if a==numb[1]:
    print(2)
if a==numb[2]:
    print(3)
if a==numb[3]:
    print(4)
else:
    print("That is not in the list")