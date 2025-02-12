class Store():
    def __init__(self, name:str, address:str):
        self.name = name
        self.address = address
        self.items = {}

    def add(self,product:str, price:float):
        if not product in self.items:
            self.items[product] = price
            print(f'Товар "{product}" успешно добавлен в магазин {self.name}')
        else:
            print('Такой товар уже имеется в магазине')

    def get_price(self, product:str):
        if product in self.items:
            return  self.items[product]
        else:
            return 'Товар отсутствует'

    def update(self, product:str, price:float):
        if product in self.items:
            self.items[product] = price
            print(f'Товар "{product}" успешно изменен')
        else:
            print('Такого товара нет в магазине')

    def delete(self, product:str):
        if product in self.items:
            self.items.pop(product)
            print(f"{product} успешно удален")

    def show_price(self):
        print('Цены в магазине', self.name)
        for key, price in self.items.items():
            print(key,'=',price)



shop1 = Store('Парус', "адрес магазина такой то")
shop1.add('Селедка',100)
shop1.add('Окунь',200)
shop1.add('Муксун',600)
shop1.add('Омуль',650)
shop1.add('Кета',500)
shop1.add('Сайра',50)

shop2 = Store('Винтаж', "Мирный")
shop2.add('Телефон',1000)
shop2.add('Стол №1',2000)
shop2.add('Стул',6000)
shop2.add('Табуретка',6500)
shop2.add('Стол №2',5000)
shop2.add('Чемодан',5000)

shop2 = Store('Молочная деревня', "Комсомольская")
shop2.add('Молоко',1000)
shop2.add('Кефир',2000)
shop2.add('Сметана 30%',6000)
shop2.add('Сметана 25%',6500)
shop2.add('Сметана 40%',5000)
shop2.add('Йогурт',5000)

shop1.show_price()
shop1.add("Икра кежуч", 1500)
shop1.show_price()
print(shop1.get_price("Икра кежуч"))
print(shop1.get_price("Икра"))
shop2.show_price()
shop2.update("Йогурт", 80)
shop2.delete('Кефир')
shop2.show_price()


