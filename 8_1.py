# Класс Time
# __init__ - принимает 2 аргумента: start_time: str (10:00). end_time: str (19:00), delta: str (0:30)
# get_timeline — возвращает график в виде списка от start_time до end_time с шагом delta
# 10:00
# 10:30
# 11:00
# ….
# 16:00
# 16:30
# 19:00
# если все временные промежутки заняты, должно быдавать строку «СВОБОДНОГО
# ВРЕМЕНИ НЕТ»
# reserve_time — принимает аргумент _time: str (11:30), данное время, если оно есть в timeline,
# должно быть от туда вычеркнуто (то есть вызывая get_timeline еще раз, там его не должно
# быть)

from datetime import datetime, timedelta


class Time:
    def __init__(self, start_time: str, end_time: str, delta: str):  # создаем объект времени, передаем параметры
        self._time_list = list()  # создаем лист

        self.start_time = datetime.strptime(start_time, "%H:%M")  # переводим все в дататайм
        self.end_time = datetime.strptime(end_time, "%H:%M")

        delta = [int(i) for i in delta.split(":")]  # делим на части
        self.delta = timedelta(hours=delta[0], minutes=delta[1])  # а вот и части

        self._create_time_list()  # создаем таймлист

    def _convert_to_str(cls, dt):
        return datetime.strftime(dt, "%H:%M") # все в стринг, нам все еще нужен стринг

    def _create_time_list(self):
        temp_time = self.start_time
        while temp_time <= self.end_time: #пока не закончится нужный период времени
            self._time_list.append(self._convert_to_str(temp_time))
            temp_time += self.delta # прибавляем к времени дельту до тех пор пока время не дойдет до нужного конца периода (19.00)

    def get_timeline(self):
        # new = [self._convert_to_str(i) for i in self._time_list]
        return self._time_list

    def reserve_time(self, _time):  # резервируем время и удаляем из списка доступных
        if _time in self._time_list:
            self._time_list.remove(_time)


a = Time(start_time='10:00', end_time='19:00', delta="0:30")  # наши данные о времени
print(a.get_timeline()) #просто список времени
a.reserve_time("12:00")
print(a.get_timeline()) # список без зарезервированного времени
