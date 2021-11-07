w=input("введите имя первого человека: ")
y=input("введите имя второго человека: ")
t=input("введите имя третьего человека: ")
names=[w,y,t]
while True:
    word=input("Хотите позвать еще одного человека?(yes/no)")
    if word=="yes":
        o=input("Введите имя человека, которого хотите позвать: ")
        names.append(o)
    if word=="no":
        break;
print(len(names))
print(names)
while True:
    word=input("Введите имя человека из списка")
    k=(names.index(word))
    print(k+1)
    jaba=input("Хотите ли чтобы этот человек присутсвовал на вечеринке(yes/no)")
    if word=="no":
        names.pop(k)
        break;
    elif word=="yes":
        break;
    else:
        break;
print(names)