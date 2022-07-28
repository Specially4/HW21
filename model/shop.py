from model.abstract.abstract_model import AbstractStorage


class Shop(AbstractStorage):
    def __init__(self, items=None, capacity: int = 20) -> None:
        super().__init__(items, capacity)
        if items is None:
            items = {}

    def add(self, name: str, count: int) -> None:
        if name in self._items.keys():
            self._items[name] = self._items[name] + count
            self._capacity -= count
        else:
            self._items[name] = count
            self._capacity -= count

    def remove(self, name: str, count: int) -> None:
        self._items[name] = self._items[name] - count
        self._capacity += count

    @property
    def free_space(self) -> int:
        """Возвращает количество свободных мест"""

        return self._capacity

    @free_space.setter
    def free_space(self, new_value):
        self._capacity = new_value

    @property
    def items(self) -> dict:
        """Возвращает содержимое склада в виде словаря"""

        return self._items

    @items.setter
    def items(self, new_value):
        self._items = new_value

    def get_unique_items_count(self, item) -> int:
        """Возвращает количество уникальных позиций"""

        return self._items[item]

    def _check_free_space(self, count: int) -> bool:
        if 20 >= self._capacity + count >= 0:
            return True
        return False

    def _max_position(self) -> bool:
        if len(self._items) <= 5:
            return True
        return False
