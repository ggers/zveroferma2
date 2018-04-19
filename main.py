# Необходимо реализовать классы животных на ферме:

# Коровы, козы, овцы, свиньи;
# Утки, куры, гуси.
# Условия:

# Должен быть один базовый класс, который наследуют все остальные животные.
# Базовый класс должен определять общие характеристики и интерфейс.

# допустим, мы будем делать заготовку для игры весёлая ферма, её животноводческая часть.
# у каждой зверюшки будет основные характеристики "вес" "запас корма". А также позиция в некоем виртуальном пастбище. исходное животное умеет получать корм (feed) и поедать этот корм, толстея на вес еды (eat). Позиция и передвижение оставляем про запас, для реализации условными коллегами. 


class animal:
    weight = None
    position = None
    food = None

    def feed(self, f):
        if food is None:
                food = 0
        food += f
    return

    def eat(self, f):
        weight += f
        food -= f
    return
# position 
    def move_to(self, destX, destY):
    return

# исходный зверь весит 10 килограмм и находится по адресу 10.10.
    def __init__(self, w=10, x=10, y=10):
        weight = w
        food = 0
        position = [x, y]
    return

# млекопитающие по сравнению с просто животным научились генерировать молоко.
class mammal(animal):
    milk = 0
    def produce_milk(self, m):
        weight -= m
        milk += m
    return

class cow(mammal):
    pass

class goat(mammal):
    pass

# овцы дополнительно научились производить шерсть.

class sheep(mammal):
    wool = 0
    def produce_wool(self, m):
        weight -= m
        milk += m
    return
    pass

# однако свиньи молоко генерировать категорически не хотят, переопределяем родительский метод.

class pig(mammal):
    def milk(self):
    return 0

# Переходим к птицам. Птицы умеют производить яйца.

class bird(animal):
    eggs = 0
    def produce_eggs(self, e):
        weight -= e
        eggs += e
    return

# утки несут яйца точно также как "птица вообще"

class duck(bird):
    pass

# куры способны снести вдвое больше яиц

class hen(bird):
    def produce_eggs(self, e):
        weight -= e
        eggs += 2*e
    return
    pass

# а вот гусям приходится тяжело и они худеют от расстройства.

class goose(bird):
    def produce_eggs(self, e):
        weight -= e
        eggs += e
        weight -= 1
    return

# Проверяем:

b = pig()
print ("Создан проверочный поросенок весом", b.weight)
a = pig()
a.weight = 15
print ("Создан проверочный поросенок весом", a.weight)
a.produce_milk
print ("Поросенок способен произвести", a.milk, "молока")

