class InfoMessage:
    """Информационное сообщение о тренировке."""
    def __init__(self,
                 training_type: str,
                 duration: float,
                 distance: float,
                 speed: float,
                 calories: float) -> None:
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def get_message(self) -> str:
        """Возвращает строку инфы."""
        message: str = (f'Тип тренировки: {self.training_type}; '
                        f'Длительность: {self.duration:.3f} ч.; '
                        f'Дистанция: {self.distance:.3f} км; '
                        f'Ср. скорость: {self.speed:.3f} км/ч; '
                        f'Потрачено ккал: {self.calories:.3f}.')
        return message


class Training:
    """Базовый класс тренировки."""
    LEN_STEP: float = 0.65
    M_IN_KM: int = 1000

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        return self.action * self.LEN_STEP / self.M_IN_KM

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return self.get_distance() / self.duration

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""

        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage(self.__class__.__name__, self.duration,
                           self.get_distance(),
                           self.get_mean_speed(), self.get_spent_calories())


class Running(Training):
    """Тренировка: бег."""

    running_calorie_multiplier_1 = 18
    running_calorie_multiplier_2 = 20
    hours_to_minutes = 60

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        return ((self.running_calorie_multiplier_1 * self.get_mean_speed()
                - self.running_calorie_multiplier_2)
                * self.weight / self.M_IN_KM
                * self.duration * self.hours_to_minutes)


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    def __init__(self, action: int, duration: float,
                 weight: float, height: int) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> float:
        """Получение затраченных калорий при ходьбе."""
        calories_3: float = 0.035
        calories_4: float = 0.029
        time_min: int = 60
        return ((calories_3 * self.weight
                + (super().get_mean_speed() ** 2 // self.height)
                * calories_4 * self.weight)
                * (self.duration * time_min))


class Swimming(Training):
    """Тренировка: плавание."""
    LEN_STEP: float = 1.38

    def __init__(self, action: int, duration: float,
                 weight: float, length_pool: int,
                 count_pool: int) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_mean_speed(self):
        """Получаем среднюю скорость движения в бассейне."""
        return ((self.length_pool * self.count_pool / Training.M_IN_KM)
                / self.duration)

    def get_spent_calories(self) -> float:
        """Получим затраченные калории при плавании"""
        calories_5: float = 1.1
        calories_6: int = 2
        return ((Swimming.get_mean_speed(self) + calories_5)
                * (calories_6) * (self.weight))


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    decoder = {'RUN': Running,
               'SWM': Swimming,
               'WLK': SportsWalking}
    return decoder[workout_type](*data)


def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info()
    print(info.get_message())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
