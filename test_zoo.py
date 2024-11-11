import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(5), 50)
       
    # Add your additional test cases here.
    def test_UnderZero_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(-3), "Invalid Input")
    def test_ticket_price_class2(self):
        self.assertEqual(self.zoo.get_ticket_price(10), 50)
    def test_ticket_price_class3(self):
        self.assertEqual(self.zoo.get_ticket_price(20), 100)
    def test_ticket_price_class4(self):
        self.assertEqual(self.zoo.get_ticket_price(22), 150)
    def test_ticket_price_class5(self):
        self.assertEqual(self.zoo.get_ticket_price(100), 100)
    
    def test_Bound1_ticket_price_(self):
        self.assertEqual(self.zoo.get_ticket_price(-1), "Invalid Input")
    def test_Bound2_ticket_price_(self):
        self.assertEqual(self.zoo.get_ticket_price(0), 50)
        self.assertEqual(self.zoo.get_ticket_price(1), 50)
        self.assertEqual(self.zoo.get_ticket_price(11), 50)
        self.assertEqual(self.zoo.get_ticket_price(12), 50)
    def test_Bound3_ticket_price_(self):
        self.assertEqual(self.zoo.get_ticket_price(13), 100)
        self.assertEqual(self.zoo.get_ticket_price(14), 100)
        self.assertEqual(self.zoo.get_ticket_price(19), 100)
        self.assertEqual(self.zoo.get_ticket_price(20), 100)
    def test_Bound4_ticket_price_(self):
        self.assertEqual(self.zoo.get_ticket_price(21), 150)
        self.assertEqual(self.zoo.get_ticket_price(22), 150)
        self.assertEqual(self.zoo.get_ticket_price(59), 150)
        self.assertEqual(self.zoo.get_ticket_price(60), 150)
    def test_Bound5_ticket_price_(self):
        self.assertEqual(self.zoo.get_ticket_price(61), 100)    
if __name__ == '__main__':
    unittest.main()