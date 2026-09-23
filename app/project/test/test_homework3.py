from hm3_model_shopping_cart import ShoppingCart


class TestShoppingCart:

    def test_add(self, shopping_cart: ShoppingCart):
        shopping_cart.add_item(name="Куртка", price=300, quantity=1)
        shopping_cart.add_item(name="Шапка", price=100, quantity=2)
        shopping_cart.add_item(name="Шкарпетки", price=50, quantity=4)
        shopping_cart.add_item(name="Книга біологія 10 клас", price=150, quantity=1)

    def test_remove(self, shopping_cart: ShoppingCart):
        shopping_cart.remove_item(name="Куртка")

    def test_get_summa(self, shopping_cart: ShoppingCart):
        assert shopping_cart.get_summa() == 550
