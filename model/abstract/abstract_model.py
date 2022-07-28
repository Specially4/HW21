from abc import ABC, abstractmethod


class AbstractStorage(ABC):
    def __init__(self, items: dict, capacity: int) -> None:
        self._items = items
        self._capacity = capacity

    @abstractmethod
    def add(self, name: str, count: int) -> None:
        if name in self._items.keys():
            self._items[name] = self._items[name] + count
            self._capacity -= count
        else:
            self._items[name] = count
            self._capacity -= count

    @abstractmethod
    def remove(self, name: str, count: int) -> None:
        self._items[name] = self._items[name] - count
        self._capacity += count

    @property
    @abstractmethod
    def free_space(self) -> int:
        """Возвращает количество свободных мест"""

        return self._capacity

    @free_space.setter
    def free_space(self, new_value):
        self._capacity = new_value

    @property
    @abstractmethod
    def items(self) -> dict:
        """Возвращает содержимое склада в виде словаря"""

        return self._items

    @items.setter
    def items(self, new_value):
        self._items = new_value

    @abstractmethod
    def get_unique_items_count(self, item) -> int:
        """Возвращает количество уникальных позиций"""

        return self._items[item]

    @abstractmethod
    def _check_free_space(self, count: int) -> bool:
        if self._capacity + count >= 0:
            return True
        return False

    @abstractmethod
    def _max_position(self) -> bool:
        return True
