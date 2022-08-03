from abc import ABC, abstractmethod


class AbstractStorage(ABC):
    def __init__(self, items: dict, capacity: int) -> None:
        self._items = items
        self._capacity = capacity

    @abstractmethod
    def add(self, name: str, count: int) -> None:
        pass

    @abstractmethod
    def remove(self, name: str, count: int) -> None:
        pass

    @property
    @abstractmethod
    def free_space(self) -> int:
        """Возвращает количество свободных мест"""

        pass

    @free_space.setter
    def free_space(self, new_value):
        pass

    @property
    @abstractmethod
    def items(self) -> dict:
        """Возвращает содержимое склада в виде словаря"""

        pass

    @items.setter
    def items(self, new_value):
        pass

    @abstractmethod
    def get_unique_items_count(self, item) -> int:
        """Возвращает количество уникальных позиций"""

        pass

    @abstractmethod
    def _check_free_space(self, count: int) -> bool:
        if self._capacity + count >= 0:
            return True
        pass

    @abstractmethod
    def _max_position(self) -> bool:
        pass
