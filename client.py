class Customer:
    def __init__(self, name, surname, patronymic, adres, credit, bank):
        self.__name = name
        self.__surname = surname
        self.__patronymic = patronymic
        self.__credit = credit
        self.__adres = adres
        self.__bank = bank
    def add(self):
        x=input('Выберите что хотите добавить')
        if x := 'Имя':
            self.__name = input()
        elif x == 'Фамилия':
            self.__surname = input()
        elif x == 'Отчество':
            self.__patronymic = input()
        elif x == 'Адрес':
            self.__adres = input()
        elif x == 'Номер карты':
            self.__credit = input()
        elif x == 'Банковский счет':
            self.__bank = input()
    def get(self):
        x=input('Выберите что хотите получить')
        if x := 'Имя':
            return self.__name
        elif x == 'Фамилия':
            return self.__surname
        elif x == 'Отчество':
            return self.__patronymic
        elif x == 'Адрес':
            return self.__adres
        elif x == 'Номер карты':
            return self.__credit
        elif x == 'Банковский счет':
            return self.__bank

     def getinfo(self):
        print("Имя: " + self.__name + " Фамилия: " + self.__surname + " Отчество: " + self.__patronymic + " Адрес: " + self.__adres + " Номер банковской карты: " + self.__credit + " Банковский счет: " + self.__bank)


newCustomer = Customer(name='', surname='', patronymic='', adres='', credit='', bank='')
newCustomer.add(newCustomer)
newCustomer.add(newCustomer)
newCustomer.add(newCustomer)
newCustomer.add(newCustomer)
newCustomer.add(newCustomer)
newCustomer.add(newCustomer)
newCustomer.get(newCustomer)
newCustomer.getinfo(newCustomer)