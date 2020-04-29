import random


class Ant:
    def __init__(self, combinations, items):
        self.combinations = combinations
        self.items = items
        self.number_of_ants = 500000

        # ініціалізація коефіцієнтів, які потрібні для розрахунків
        self.tau = 1
        self.eta = 1
        self.p_coef = 0.2
        self.b = 1
        self.a = 1
        self.q = 1

        self.statistics = {}

        self.__make_data()

    # метод, що з матриці міст утворює масив ребер з необхідними параметрами
    def __make_data(self):
        self.data = []
        for combination in self.combinations:
            first_id = combination['id']
            for connection in combination['connections']:
                second_id = connection['id']
                exist = False
                for item in self.data:
                    if first_id in item['rib'] and second_id in item['rib']:
                        exist = True
                        break
                if not exist:
                    self.data.append({
                        'rib': (first_id, second_id),
                        'distance': connection['distance'],
                        'eta': self.eta / connection['distance'],
                        'tau': self.tau,
                    })

    # метод, що знаходить міста, в які мураха може перейти
    def __find_possible_items(self, t_list):
        p = []  # можливі міста для переходу
        p_sum = 0
        for item in self.data:  # перебираємо ребра
            if t_list[-1] in item['rib']:  # якщо ребро містить місто, в якому мураха зараз знаходиться
                rib_list = list(item['rib'])
                rib_list.remove(t_list[-1])
                if rib_list[0] not in t_list:  # якщо ребро містить місто в якому мураха ще не була
                    value = pow(item['eta'], self.b) * pow(item['tau'], self.a)
                    p_sum += value
                    p.append({'next_city': rib_list[0], 'value': 100 * value})
        return p, p_sum

    # метод, що обирає одне місто з запропонованих
    @staticmethod
    def __find_next_item(p, p_sum, t_list):
        rand_value = random.random() * 100
        p_range = 0
        for i in range(len(p)):
            p[i]['value'] /= p_sum
            p_range += p[i]['value']
            if rand_value <= p_range:
                t_list.append(p[i]['next_city'])
                break

        if p_range < 100 and rand_value == 100:
            t_list.append(p[-1]['next_city'])

    # метод для отримання дистанції між містами
    def __get_distance(self, t_list):
        distance = 0
        for i in range(len(t_list) - 1):
            for item in self.data:
                if t_list[i] in item['rib'] and t_list[i + 1] in item['rib']:
                    distance += item['distance']
        return distance

    # метод для оновлення феромонів
    def __update_ribs(self, t_list):
        distance = self.__get_distance(t_list)  # отримуємо пройдену дистанцію
        delta_t = self.q / distance
        for i in range(len(t_list) - 1):
            for item in self.data:
                if t_list[i] in item['rib'] and t_list[i + 1] in item['rib']:
                    item['tau'] = (1 - self.p_coef) * item['tau'] + delta_t  # оновлюємо феромон на ребрі

        return distance

    # метод для збору статистики
    def __make_statistics(self, t_list, distance, ant):
        path = ' - '.join([str(self.items[item]) for item in t_list])  # створюємо пройдений маршрут
        if not self.statistics.get(path):
            self.statistics[path] = {
                'first_10': 0,
                'first_50': 0,
                'last_50': 0,
                'last_10': 0,
                'all': 0,
                'distance': distance
            }

        self.statistics[path]['all'] += 1
        if ant < (self.number_of_ants / 2):
            self.statistics[path]['first_50'] += 1
            if ant <= (self.number_of_ants / 10):
                self.statistics[path]['first_10'] += 1
        else:
            self.statistics[path]['last_50'] += 1
            if ant >= ((self.number_of_ants * 9) / 10):
                self.statistics[path]['last_10'] += 1

    # метод для запуску розв'язання
    def run(self):
        for ant in range(self.number_of_ants):
            t_list = [random.choice(list(self.items.keys()))]  # обираємо початкове місто

            while True:
                p, p_sum = self.__find_possible_items(t_list)  # знаходимо можливі шляхи
                if len(p) == 0:  # якщо можливих шляхів не має, то це означає, що мураха побувала у всіх містах
                    # додаємо у список відвіданих міст початкову позиція(щоб повернутися туди звідки почали рух)
                    t_list.append(t_list[0])
                    distance = self.__update_ribs(t_list)  # оновлюємо феромони та отримуємо пройдену дистанцію
                    self.__make_statistics(t_list, distance, ant)  # оновлюємо статистику

                    print(f'Ant number {ant + 1} has finished his work. Distance = {distance}')
                    break

                self.__find_next_item(p, p_sum, t_list)  # обираємо наступне місто з списку можливих шляхів
