import unittest
from src.customer import Customer
from src.drink import Drink
from src.pub import Pub


class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Pedro Sanchez", 50, [], 50.0)
        self.broke_customer = Customer("CodeClan Student", 30, [], 1.0)
        self.drink_1 = Drink("Mahou", 5.0, 5)
        self.drink_2 = Drink("Coca-Cola", 2.0, 0)
        self.pub = Pub("El Tigre", 1000.0, [self.drink_1, self.drink_2])

    def test_customer_name(self):
        self.assertEqual("Pedro Sanchez", self.customer.name)

    def test_customer_stomach(self):
        self.assertEqual([], self.customer.stomach)

    def test_customer_wallet(self):
        self.assertEqual(50.0, self.customer.wallet)

    def test_buy_drink(self):
        self.customer.buy_drink(self.pub, "Mahou")
        self.assertEqual(45.0, self.customer.wallet)
        self.assertEqual(1005.0, self.pub.till)
        self.assertEqual(1, self.customer.get_stomach_count())
        self.assertEqual(1, self.pub.get_stock_count())

    def test_alcohol_level(self):
        self.assertEqual(0, self.customer.drunkenness)
        self.customer.buy_drink(self.pub, "Mahou")
        self.assertEqual(5, self.customer.drunkenness)

    def test_can_afford(self):
        self.assertEqual(True, self.customer.can_afford(self.drink_1))
        self.assertEqual(False, self.broke_customer.can_afford(self.drink_1))

    def test_buy_drink_no_money(self):
        self.assertEqual("Not enough money",
                         self.broke_customer.buy_drink(self.pub, "Coca-Cola"))
