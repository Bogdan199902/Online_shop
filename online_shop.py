# user -> administrator
# user <- order (<- order details ->) item (<- item_list ->) catalog <- catalog!
class User(object):
    def __init__(self, id, name, surname):
        self.id = id
        self.name = name
        self.surname = surname

    def get_name(self):
        return self.name


class Admin(User):
    def __init__(self, id, name, surname, activity_area):
        super().__init__(id, name, surname)
        self.activity_area = activity_area  # Возврат или бан

    def return_choices(self, all_orders, for_return):  # Возврат
        all_orders.remove(for_return)
        print('Возврат осуществлен')
        return all_orders

    def delet(self, user_for_ban, ban_list, all_users):  # Бан
        print('Был забанен юзер')
        ban_list.append(user_for_ban)
        all_users.remove(str(user_for_ban))
        return ban_list, all_users


class Order(object):
    def __init__(self, id, user):
        self.id = id
        self.user = user

    def get_id(self):
        return self.id

    def return_order(self, for_return, all_orders):
        print('Вы уверены, что хотите вернуть заказ? (Да/Нет)')
        mark = input()
        if mark == 'Да':
            print('Заявка на отмену заказа создана')
            res_list = Admin.return_choices(all_orders, for_return)
            return res_list
        else:
            print('Отмена запроса')


class OrderDetails(object):
    def __init__(self, id, order, item_list, sum_order):
        self.id = id
        self.order = order
        self.item_list = item_list
        self.sum_order = sum_order


class Item(object):
    def __init__(self, id, title, price):
        self.id = id
        self.title = title
        self.price = price

    def get_title(self):
        return self.title

    def solve_price(self):
        return self.price


class ItemsList(object):
    def __init__(self, id, item):
        self.id = id
        self.item = item


class Magazine(object):
    def __init__(self, id, items):
        self.id = id
        self.items = items


# users and admins
us1 = User(1, 'Bogdan', 'Belenov')
us2 = User(2, 'Aslan', 'Mamedov')
us3 = User(3, 'John', 'Culen')
adm1 = Admin(4, 'Govard', 'Stark', 'admin')
adm2 = Admin(5, 'Captain', 'America', 'admin')

# item, item_list, magazine
item1 = Item(1, 'Паста', 100)
item2 = Item(2, 'Утюг', 500)
item3 = Item(3, 'Масло', 200)
item4 = Item(4, 'Хлеб', 80)
item5 = Item(5, 'Молоко', 70)
item6 = Item(6, 'Печенье', 50)

item_list1 = ItemsList(1, [Item.get_title(item1), Item.get_title(item2), Item.get_title(item3)])
item_list2 = ItemsList(2, [Item.get_title(item4), Item.get_title(item5), Item.get_title(item6)])

magazine1 = Magazine(1, [Item.get_title(item3), Item.get_title(item4), Item.get_title(item1)])
magazine2 = Magazine(2, [Item.get_title(item2), Item.get_title(item5), Item.get_title(item6)])

# order, order_details
order1 = Order(1, us1)
order2 = Order(2, us2)
describe_order1 = OrderDetails(1, Order.get_id(order1),
                               [Item.get_title(item1), Item.get_title(item2), Item.get_title(item3)],
                               (Item.solve_price(item1)+Item.solve_price(item2)+Item.solve_price(item3)))
describe_order2 = OrderDetails(2, Order.get_id(order2),
                               [Item.get_title(item4), Item.get_title(item5), Item.get_title(item6)],
                               (Item.solve_price(item4)+Item.solve_price(item5)+Item.solve_price(item6)))

# clear_lists
list_with_all_users = [User.get_name(us1), User.get_name(us2), User.get_name(us3)]
list_with_all_orders = [[Item.get_title(item1), Item.get_title(item2), Item.get_title(item3)],
                        [Item.get_title(item4), Item.get_title(item5), Item.get_title(item6)]]
list_with_users_in_ban = []
