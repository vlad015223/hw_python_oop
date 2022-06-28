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
    HOURS_TO_MINUTES = 60

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
        raise NotImplementedError

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage(self.__class__.__name__,
                           self.duration,
                           self.get_distance(),
                           self.get_mean_speed(),
                           self.get_spent_calories())


class Running(Training):
    """Тренировка: бег."""

    RUNNING_CALORIE_MULTIPLIER_1 = 18
    RUNNING_CALORIE_MULTIPLIER_2 = 20

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        calorie_per_minute = (
            (
                self.RUNNING_CALORIE_MULTIPLIER_1 * self.get_mean_speed()
                - self.RUNNING_CALORIE_MULTIPLIER_2
            ) * self.weight / self.M_IN_KM
        )
        return calorie_per_minute * self.duration * self.HOURS_TO_MINUTES


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""

    CALORIES_3: float = 0.035
    CALORIES_4: float = 0.029

    def __init__(self, action: int,
                 duration: float,
                 weight: float,
                 height: int) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> float:
        """Получение затраченных калорий при ходьбе."""
        calorie_per_minute_2 = (
            (
                self.CALORIES_3 * self.weight
                + (self.get_mean_speed() ** 2 // self.height)
                * self.CALORIES_4 * self.weight
            )
        )
        return calorie_per_minute_2 * self.duration * self.HOURS_TO_MINUTES


class Swimming(Training):
    """Тренировка: плавание."""

    CALORIES_5: float = 1.1
    CALORIES_6: int = 2
    LEN_STEP: float = 1.38

    def __init__(self, action: int,
                 duration: float,
                 weight: float,
                 length_pool: int,
                 count_pool: int) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_mean_speed(self):
        """Получаем среднюю скорость движения в бассейне."""
        return ((self.length_pool * self.count_pool / self.M_IN_KM)
                / self.duration)

    def get_spent_calories(self) -> float:
        """Получим затраченные калории при плавании"""
        calorie_per_minute_3 = (
            self.get_mean_speed() + self.CALORIES_5
        )
        return calorie_per_minute_3 * self.CALORIES_6 * self.weight


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    workout_class_type = {'RUN': Running,
                          'WLK': SportsWalking,
                          'SWM': Swimming}
    if workout_type not in workout_class_type:
        raise ValueError(
            f'Тренировки {workout_type} не существует.')
    return workout_class_type[workout_type](*data)


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
