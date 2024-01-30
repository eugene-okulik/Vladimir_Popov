from random import randint


class Flower:

    def __init__(self, name, colour, type, freshness, length, lifetime, price):
        self.id = randint(0, 10000)
        self.name = name
        self.colour = colour
        self.type = type
        self.freshness = freshness
        self.length = length
        self.lifetime = lifetime
        self.price = price


class Rose(Flower):

    def __init__(self, name, colour, type, freshness, length, lifetime, price):
        super().__init__(name, colour, type, freshness, length, lifetime, price)


class Peony(Flower):

    def __init__(self, name, colour, type, freshness, length, lifetime, price):
        super().__init__(name, colour, type, freshness, length, lifetime, price)


class Tulip(Flower):

    def __init__(self, name, colour, type, freshness, length, lifetime, price):
        super().__init__(name, colour, type, freshness, length, lifetime, price)


class Bouquet:

    def __init__(self, *flowers):
        self.bouquet = list(flowers)
        self.flowers_in_bouquet = self.show_flowers_in_bouquet()
        self.fading_time = self.count_fading_time()
        self.bouquet_price = self.count_bouquet_price()

    def show_info(self):
        print(f"Цветы в букете: {', '.join(self.flowers_in_bouquet)}")
        print(f"Среднее время увядания: {self.fading_time:.2f} дней")
        print(f"Цена букета: {self.bouquet_price}")

    def show_flowers_in_bouquet(self):
        self.flowers_in_bouquet = [(flower.colour, flower.name) for flower in self.bouquet]
        self.flowers_in_bouquet = list(map(lambda x: " ".join(x), self.flowers_in_bouquet))
        return self.flowers_in_bouquet

    def count_fading_time(self):
        self.fading_time = sum([flower.lifetime for flower in self.bouquet]) / len(self.bouquet)
        return self.fading_time

    def count_bouquet_price(self):
        self.bouquet_price = sum([flower.price for flower in self.bouquet])
        return self.bouquet_price

    def sort_by_freshness(self):
        self.bouquet_sorted_by_freshness = sorted(self.bouquet, key=lambda flower: flower.freshness)
        self.bouquet_sorted_by_freshness = [(flower.colour, flower.name) for flower in self.bouquet_sorted_by_freshness]
        self.bouquet_sorted_by_freshness = list(map(lambda x: " ".join(x), self.bouquet_sorted_by_freshness))
        print(f"Цветы, отсортированные по свежести: {', '.join(self.bouquet_sorted_by_freshness)}")

    def sort_by_colour(self):
        self.bouquet_sorted_by_colour = sorted(self.bouquet, key=lambda flower: flower.colour)
        self.bouquet_sorted_by_colour = [(flower.colour, flower.name) for flower in self.bouquet_sorted_by_colour]
        self.bouquet_sorted_by_colour = list(map(lambda x: " ".join(x), self.bouquet_sorted_by_colour))
        print(f"Цветы, отсортированные по цвету: {', '.join(self.bouquet_sorted_by_colour)}")

    def sort_by_length(self):
        self.bouquet_sorted_by_length = sorted(self.bouquet, key=lambda flower: flower.length)
        self.bouquet_sorted_by_length = [(flower.colour, flower.name) for flower in self.bouquet_sorted_by_length]
        self.bouquet_sorted_by_length = list(map(lambda x: " ".join(x), self.bouquet_sorted_by_length))
        print(f"Цветы, отсортированные по длине стебля: {', '.join(self.bouquet_sorted_by_length)}")

    def sort_by_price(self):
        self.bouquet_sorted_by_price = sorted(self.bouquet, key=lambda flower: flower.price)
        self.bouquet_sorted_by_price = [(flower.colour, flower.name) for flower in self.bouquet_sorted_by_price]
        self.bouquet_sorted_by_price = list(map(lambda x: " ".join(x), self.bouquet_sorted_by_price))
        print(f"Цветы, отсортированные по цене: {', '.join(self.bouquet_sorted_by_price)}")

    def find_flower_by_name(self, flower_name):
        flowers_search_list = [flower for flower in self.flowers_in_bouquet if flower_name in flower]
        if len(flowers_search_list) > 0:
            print(f"Результаты поиска по букету: {', '.join(flowers_search_list)}")
        else:
            print(f"Цветка {flower_name} нет в букете")


rose1 = Rose(name="Роза", colour="Красная", type="rose", freshness=True, length=25, lifetime=3, price=150)
rose2 = Rose(name="Роза", colour="Желтая", type="rose", freshness=False, length=25, lifetime=3, price=200)
rose3 = Rose(name="Роза", colour="Белая", type="rose", freshness=True, length=25, lifetime=3, price=250)

tulip1 = Tulip(name="Тюльпан", colour="Белый", type="tulip", freshness=True, length=15, lifetime=2, price=50)
tulip2 = Tulip(name="Тюльпан", colour="Красный", type="tulip", freshness=True, length=15, lifetime=2, price=70)
tulip3 = Tulip(name="Тюльпан", colour="Желтый", type="tulip", freshness=False, length=15, lifetime=2, price=60)

peony1 = Peony(name="Пион", colour="Белый", type="peony", freshness=False, length=20, lifetime=4, price=350)
peony2 = Peony(name="Пион", colour="Желтый", type="peony", freshness=True, length=20, lifetime=4, price=300)
peony3 = Peony(name="Пион", colour="Алый", type="peony", freshness=True, length=30, lifetime=4, price=300)


bouquet1 = Bouquet(peony1, peony3, rose1)
bouquet1.show_info()
bouquet1.find_flower_by_name("Роза")
bouquet1.sort_by_freshness()
bouquet1.sort_by_colour()
bouquet1.sort_by_length()
bouquet1.sort_by_price()
