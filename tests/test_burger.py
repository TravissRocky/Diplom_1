from unittest.mock import Mock

import pytest

from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:
    """Тесты для класса Burger."""

    def test_burger_init(self):
        """Тест инициализации бургера."""
        burger = Burger()
        assert burger.bun is None
        assert burger.ingredients == []

    def test_burger_set_buns(self):
        """Тест метода set_buns."""
        burger = Burger()
        mock_bun = Mock(spec=Bun)
        mock_bun.get_name.return_value = 'black bun'
        mock_bun.get_price.return_value = 100
        
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_burger_add_ingredient(self):
        """Тест метода add_ingredient."""
        burger = Burger()
        mock_ingredient = Mock(spec=Ingredient)
        mock_ingredient.get_name.return_value = 'cutlet'
        mock_ingredient.get_price.return_value = 100
        
        burger.add_ingredient(mock_ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient

    def test_burger_add_multiple_ingredients(self):
        """Тест добавления нескольких ингредиентов."""
        burger = Burger()
        mock_ingredient1 = Mock(spec=Ingredient)
        mock_ingredient2 = Mock(spec=Ingredient)
        mock_ingredient3 = Mock(spec=Ingredient)
        
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        burger.add_ingredient(mock_ingredient3)
        
        assert len(burger.ingredients) == 3

    def test_burger_remove_ingredient(self):
        """Тест метода remove_ingredient."""
        burger = Burger()
        mock_ingredient1 = Mock(spec=Ingredient)
        mock_ingredient2 = Mock(spec=Ingredient)
        mock_ingredient3 = Mock(spec=Ingredient)
        
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        burger.add_ingredient(mock_ingredient3)
        
        burger.remove_ingredient(1)
        assert len(burger.ingredients) == 2
        assert burger.ingredients[0] == mock_ingredient1
        assert burger.ingredients[1] == mock_ingredient3

    def test_burger_move_ingredient(self):
        """Тест метода move_ingredient."""
        burger = Burger()
        mock_ingredient1 = Mock(spec=Ingredient)
        mock_ingredient1.get_name.return_value = 'cutlet'
        mock_ingredient2 = Mock(spec=Ingredient)
        mock_ingredient2.get_name.return_value = 'sausage'
        mock_ingredient3 = Mock(spec=Ingredient)
        mock_ingredient3.get_name.return_value = 'dinosaur'
        
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        burger.add_ingredient(mock_ingredient3)
        
        burger.move_ingredient(2, 0)
        assert burger.ingredients[0] == mock_ingredient3
        assert burger.ingredients[1] == mock_ingredient1
        assert burger.ingredients[2] == mock_ingredient2

    @pytest.mark.parametrize('bun_price,ingredient_prices,expected_price', [
        (100, [100, 200], 500),  # 100*2 + 100 + 200 = 500
        (200, [100], 500),  # 200*2 + 100 = 500
        (150, [50, 75, 100], 525),  # 150*2 + 50 + 75 + 100 = 525
    ])
    def test_burger_get_price(self, bun_price, ingredient_prices, expected_price):
        """Тест метода get_price с параметризацией."""
        burger = Burger()
        mock_bun = Mock(spec=Bun)
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)
        
        for price in ingredient_prices:
            mock_ingredient = Mock(spec=Ingredient)
            mock_ingredient.get_price.return_value = price
            burger.add_ingredient(mock_ingredient)
        
        assert burger.get_price() == expected_price

    def test_burger_get_receipt(self):
        """Тест метода get_receipt."""
        burger = Burger()
        mock_bun = Mock(spec=Bun)
        mock_bun.get_name.return_value = 'black bun'
        mock_bun.get_price.return_value = 100
        burger.set_buns(mock_bun)
        
        mock_ingredient1 = Mock(spec=Ingredient)
        mock_ingredient1.get_type.return_value = INGREDIENT_TYPE_FILLING
        mock_ingredient1.get_name.return_value = 'cutlet'
        mock_ingredient1.get_price.return_value = 100
        
        mock_ingredient2 = Mock(spec=Ingredient)
        mock_ingredient2.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_ingredient2.get_name.return_value = 'hot sauce'
        mock_ingredient2.get_price.return_value = 200
        
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        
        receipt = burger.get_receipt()
        assert '(==== black bun ====)' in receipt
        assert '= filling cutlet =' in receipt
        assert '= sauce hot sauce =' in receipt
        assert 'Price: 500' in receipt

    def test_burger_get_price_without_bun(self):
        """Тест get_price без установленной булочки."""
        burger = Burger()
        mock_ingredient = Mock(spec=Ingredient)
        mock_ingredient.get_price.return_value = 100
        burger.add_ingredient(mock_ingredient)
        
        # Если bun не установлен, вызов get_price() вызовет AttributeError
        # Это нормальное поведение, так как в коде есть обращение к self.bun.get_price()
        with pytest.raises(AttributeError):
            burger.get_price()

