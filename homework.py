class InfoMessage:
    """Информационное сообщение о тренировке."""
    def __init__(self, training_type: str, duration: float, distance: float,
        speed: float, calories: float) -> None:
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def get_message(self) -> str:
        """Возвращает строку сообщения"""
        return (f'Тип тренировки: {self.training_type};'
                'Длительность: {self.duration} ч.;'
                'Дистанция: {self.distance} км;'
                'Ср. скорость: {self.speed} км/ч;'
                'Потрачено ккал: {self.calories}.')


class Training:
    """Базовый класс тренировки."""
    LEN_STEP = float = 0.65
    M_IN_KM = int = 1000

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        pass

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        #action * LEN_STEP / M_IN_KM, action = количество действий(шаги, гребки)

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        #преодоленная_дистанция_за_тренировку / время_тренировки 

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        #Логика подсчета калорий для каждого вида тренировки будет своя, 
        #поэтому в базовом классе не нужно описывать поведение метода, в его теле останется ключевое слово pass.
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        #возвращает объект класса сообщения

class Running(Training):
    """Тренировка: бег."""
    pass


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    pass


class Swimming(Training):
    """Тренировка: плавание."""
    pass


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    pass


def main(training: Training) -> None:
    """Главная функция."""
    pass


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)

