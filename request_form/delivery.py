import re

from config.error_config import NotEnoughTo, NotEnoughFrom


class Request:
    def __init__(self, user_str: str) -> None:
        self._from: str = ''
        self._to: str = ''
        self._amount: int = 0
        self._product: str = ''
        self._delivery(self._make_list_delivery(user_str))

    def __repr__(self):
        return f'\nfrom = {self._from},\nto = {self._to},\namount = {self._amount},\nproduct = {self._product}\n'

    def main(self, other_1, other_2):
        x = '\n'
        other_1.remove(self._product, self._amount)
        other_2.add(self._product, self._amount)
        return f'{self.check_item(other_1, other_2)}\n' \
               f'Курьер забрал {self._amount} {self._product} со {self._from}а\n' \
               f'Курьер везет {self._amount} {self._product} со {self._from}а в {self._to}\n' \
               f'Курьер доставил {self._amount} {self._product} в {self._to}\n' \
               f'\nВ {self._from} хранится:\n' \
               f'{x.join([f"{item} - {value}" for item, value in other_1.items.items()])}\n' \
               f'\nВ {self._to} хранится:\n' \
               f'{x.join([f"{item} - {value}" for item, value in other_2.items.items()])}\n'

    def check_item(self, other_1, other_2):
        if other_1.get_unique_items_count(self._product) >= self._amount:
            if other_2.free_space >= self._amount:
                return f'Нужное количество есть на {self._from}е'
            raise NotEnoughTo(f'В {self._to} недостаточно места, попробуйте что-то другое')
        raise NotEnoughFrom(f'Не хватает на {self._from}, попробуйте заказать меньше')

    def _delivery(self, list_req):
        self._from = list_req[list_req.index('из') + 1]
        self._to = list_req[list_req.index('в') + 1]
        for item in list_req:
            if type(item) == int:
                self._amount = item
        self._product = list_req[list_req.index(self._amount) + 1]

    @staticmethod
    def _make_list_delivery(req: str) -> list:
        list_req = re.split(";|,|\n| ", req)
        for item in list_req:
            if item == '':
                list_req.remove(item)
            if item.isdigit():
                list_req[list_req.index(item)] = int(item)

        return list_req
