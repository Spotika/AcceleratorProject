from typing import Any, Dict, List


class Adapter:
    """
    Адаптер позволяет связывать несколько объектов
    """

    data_streams: Dict[str, List[Any]] = {}
    """Поток данных, ключ - имя получателя, значение - стек из непрочитанных сообщений"""

    @classmethod
    def send_data(cls, data: Any, receiver: str) -> None:
        """
        Отправляет информацию в стек сообщений получателя
        :param data: информация
        :param receiver: имя получателя
        """

    @classmethod
    def get_next(cls, receiver: str) -> Any:
        """
        :param receiver: имя получателя
        :return: возвращает следующий непрочитанный объект данных, доставленный получателю
        """
