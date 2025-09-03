import io
import unittest
from contextlib import redirect_stdout
from Task_4 import ShoppingCart
class TestShoppingCart(unittest.TestCase):
    def test_add_single_item(self):
        cart = ShoppingCart()
        cart.add_item("apple", 1.5)
        self.assertEqual(cart.items, {"apple": [1.5]})
        self.assertAlmostEqual(cart.total_cost(), 1.5)
    def test_add_multiple_same_name(self):
        cart = ShoppingCart()
        cart.add_item("banana", 0.75)
        cart.add_item("banana", 0.80)
        self.assertEqual(cart.items["banana"], [0.75, 0.80])
        self.assertAlmostEqual(cart.total_cost(), 1.55)
    def test_remove_item_lifo_per_name(self):
        cart = ShoppingCart()
        cart.add_item("milk", 2.0)
        cart.add_item("milk", 2.5)
        cart.remove_item("milk")
        self.assertEqual(cart.items, {"milk": [2.0]})
        self.assertAlmostEqual(cart.total_cost(), 2.0)
    def test_remove_item_deletes_key_when_empty(self):
        cart = ShoppingCart()
        cart.add_item("bread", 1.25)
        cart.remove_item("bread")
        self.assertNotIn("bread", cart.items)
        self.assertAlmostEqual(cart.total_cost(), 0.0)
    def test_remove_item_nonexistent_prints_message(self):
        cart = ShoppingCart()
        buf = io.StringIO()
        with redirect_stdout(buf):
            cart.remove_item("does_not_exist")
        out = buf.getvalue()
        self.assertIn("Item 'does_not_exist' not found in cart.", out)
    def test_total_cost_multiple_items(self):
        cart = ShoppingCart()
        cart.add_item("apple", 1.0)
        cart.add_item("banana", 2.0)
        cart.add_item("banana", 3.0)
        cart.add_item("pear", 4.0)
        self.assertAlmostEqual(cart.total_cost(), 10.0)
    def test_total_cost_empty_cart_is_zero(self):
        cart = ShoppingCart()
        self.assertAlmostEqual(cart.total_cost(), 0.0)
    def test_negative_prices_are_summed_as_is(self):
        cart = ShoppingCart()
        cart.add_item("discount", -5.0)
        cart.add_item("regular", 10.0)
        self.assertAlmostEqual(cart.total_cost(), 5.0)
if __name__ == "__main__":
    unittest.main()

