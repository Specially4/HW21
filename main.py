from config.error_config import NotEnoughTo, NotEnoughFrom
from model.shop import Shop
from model.storage import Storage
from request_form.delivery import Request

shop = Shop()
storage = Storage()
storage.items = {'шоколад': 2, 'печеньки': 20, 'бананы': 10}
shop.items = {'конфетки': 3}
req = Request('Доставить 3 печеньки из склад в магазин')
try:
    print(req.main(storage, shop))
except NotEnoughTo as e:
    print(e.args[0])
except NotEnoughFrom as e:
    print(e.args[0])
    
