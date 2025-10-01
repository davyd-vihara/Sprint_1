import datetime

class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    @property
    def name_items(self):
        return self.__name_items

    @property
    def number_items(self):
        return self.__number_items

    def add_item_to_cheque(self, name_item):
        try:
            if not name_item or len(name_item) > 40:
                raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')

            if name_item not in self.__item_price:
                raise NameError('Позиция отсутствует в товарном справочнике')

            self.__name_items.append(name_item)
            self.__number_items += 1

        except ValueError as ve:
            print(ve)
        except NameError as ne:
            print(ne)

    def delete_item_from_check(self, name_item):
        try:
            if name_item not in self.__name_items:
                raise NameError('Позиция отсутствует в чеке')

            self.__name_items.remove(name_item)
            self.__number_items -= 1
        except NameError as ne:
            print(ne)

    def check_amount(self):
        total_amount = 0
        for item in self.__name_items:
            total_amount += self.__item_price[item]

        if len(self.__name_items) > 10:
            return total_amount - total_amount * 0.1
        else:
            return total_amount

    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = []
        total = []

        for item in self.__name_items:
            if self.__tax_rate.get(item) == 20:
                twenty_percent_tax.append(item)
                total.append(self.__item_price[item])

        total_amount = sum(total)

        if len(self.__name_items) > 10:
            total_amount *= 0.9

        return total_amount * 0.2

    def ten_percent_tax_calculation(self):
        ten_percent_tax = []
        total = []

        for item in self.__name_items:
            if self.__tax_rate.get(item) == 10:
                ten_percent_tax.append(item)
                total.append(self.__item_price[item])

        total_amount = sum(total)

        if len(self.__name_items) > 10:
            total_amount *= 0.9

        return total_amount * 0.1

    def total_tax(self):
        return self.ten_percent_tax_calculation() + self.twenty_percent_tax_calculation()

    @staticmethod
    def get_telephone_number(telephone_number: int):
        if not isinstance(telephone_number, int):
            raise ValueError('Необходимо ввести цифры')

        if len(str(telephone_number)) != 10:
            raise ValueError('Необходимо ввести 10 цифр после "+7"')

        return f'+7{telephone_number}'

    @staticmethod
    def get_date_and_time():
        date_and_time = []
        now = datetime.datetime.now()

        date = [
            ["часы", lambda x: x.hour],
            ["минуты", lambda x: x.minute],
            ["день", lambda x: x.day],
            ["месяц", lambda x: x.month],
            ["год", lambda x: x.year],
        ]

        for name, func in date:
            date_and_time.append(f"{name}: {func(now)}")

        return date_and_time