from typing import Optional, Tuple


class Tracker:
    """
    Класс, отслеживающий предмет
    """

    @classmethod
    def init(cls) -> None:
        """
        Инициализация трекера
        """

    @classmethod
    def update(cls) -> None:
        """
        Обновление трекера
        """

    @classmethod
    def get_pos(cls) -> Optional[Tuple[int, int]]:
        """
        :return: Позицию объекта, или None, если объекта нет
        """

    @classmethod
    def get_collision(cls) -> bool:
        """
        Определяет столкновение объекта со стеной
        :return: True, если столкновение случилось, иначе False
        """

