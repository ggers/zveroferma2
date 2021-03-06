# Необходимо реализовать классы животных на ферме:

# Коровы, козы, овцы, свиньи;
# Утки, куры, гуси.
# Условия:

# Должен быть один базовый класс, который наследуют все остальные животные.
# Базовый класс должен определять общие характеристики и интерфейс.

# допустим, мы будем делать заготовку для игры весёлая ферма, её животноводческая часть.
# у каждой зверюшки будет основные характеристики "вес" "запас корма".
# исходное животное умеет получать корм(feed) и поедать этот корм, толстея на вес еды(eat).\
# Позиция и передвижение оставляем про запас, для реализации условными коллегами.
# А также позиция в некоем виртуальном пастбище.

class Animal:
    weight = 0
    position = 0
    food = None
    name = ""

    def feed(self, f):
        self.food += f

    def eat(self, f):
        self.weight += f
        self.food -= f

    def move_to(self, destX, destY):
        return

    def __init__(self, name="NoName", w=10, f=0):
        self.weight = w
        self.food = f


 # млекопитающие по сравнению с просто животным научились генерировать молоко.
# а также мы можем сравнить их вес, переопределив операторы < и >
class Mammal(Animal):
    milk = 0

    def produce_milk(self, m):
        self.weight -= m
        self.milk += m

    def __lt__(self, other):
        return self.weight < other.weight


class Cow(Mammal):
    pass


class Goat(Mammal):
    pass


# овцы дополнительно научились производить шерсть.
class Sheep(Mammal):
    wool = 0

    def produce_wool(self, m):
        self.weight -= m
        self. milk += m


# однако свиньи молоко генерировать категорически не хотят, переопределяем родительский метод.
class Pig(Mammal):

    def milk(self):
        return 0


# Переходим к птицам. Птицы умеют производить яйца.
class Bird(Animal):
    eggs = 0

    def produce_eggs(self, e):
        self.weight -= e
        self.eggs += e


# утки несут яйца точно также как "птица вообще"
class Duck(Bird):
    pass


# куры способны снести вдвое больше яиц
class Hen(Bird):

    def produce_eggs(self, e):
        self.weight -= e
        self.eggs += 2 * e


# а вот гусям приходится тяжело и они худеют от расстройства.
class Goose(Bird):

    def produce_eggs(self, e):
        self.weight -= e
        self.eggs += e
        self.weight -= 1


# Проверяем:
pig_beta = Pig()
print("Создан проверочный поросенок Бета весом", pig_beta.weight, "\nБлагодаря инициализация вес остаётся 10 \n")

pig_alpha = Pig()
pig_alpha.weight = 15
print("Создан проверочный поросенок Альфа весом", pig_alpha.weight, "\nВручную установили вес 15\n")

pig_delta = Pig(66)
print("Создан проверочный поросенок Дельта весом", pig_delta.weight, "\nПри создании с параметром вес равен параметру 66\n")

pig_gamma = Pig()
pig_gamma.feed(20)
pig_gamma.eat(19)
print("Создан проверочный поросенок Гамма весом", pig_gamma.weight, "\nИспользуя методы класса вес равен 29\n")

print("Вес поросёнка Альфа {}, а вес поросёнка Дельта {}".format(pig_alpha.weight, pig_gamma.weight))
print("Вес поросёнка Альфа меньше веса поросёнка Дельта?", pig_alpha < pig_delta)
print("Вес поросёнка Альфа больше веса поросёнка Дельта?", pig_alpha > pig_delta)
