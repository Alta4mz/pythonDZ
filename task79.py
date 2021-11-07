nums=[]
o=0
while True:
    o+=1
    u=int(input("Введите число"))
    nums.append(u)
    if o==3:
        question=input("Хотите ли вы оставить последнее введенное число в списке?")
        if question=="no":
            nums.pop(2)
            break;
print(nums)