import pytest

from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:
    """Тесты для класса Ingredient."""

    @pytest.mark.parametrize('ingredient_type,name,price', [
        (INGREDIENT_TYPE_SAUCE, 'hot sauce', 100),
        (INGREDIENT_TYPE_SAUCE, 'sour cream', 200),
        (INGREDIENT_TYPE_FILLING, 'cutlet', 100),
        (INGREDIENT_TYPE_FILLING, 'dinosaur', 200),
    ])
    def test_ingredient_init(self, ingredient_type, name, price):
        """Тест инициализации ингредиента с различными параметрами."""
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.type == ingredient_type
        assert ingredient.name == name
        assert ingredient.price == price

    @pytest.mark.parametrize('ingredient_type,name,price', [
        (INGREDIENT_TYPE_SAUCE, 'hot sauce', 100),
        (INGREDIENT_TYPE_FILLING, 'cutlet', 100),
    ])
    def test_ingredient_get_type(self, ingredient_type, name, price):
        """Тест метода get_type."""
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type

    @pytest.mark.parametrize('ingredient_type,name,price', [
        (INGREDIENT_TYPE_SAUCE, 'hot sauce', 100),
        (INGREDIENT_TYPE_FILLING, 'cutlet', 100),
    ])
    def test_ingredient_get_name(self, ingredient_type, name, price):
        """Тест метода get_name."""
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize('ingredient_type,name,price', [
        (INGREDIENT_TYPE_SAUCE, 'hot sauce', 100),
        (INGREDIENT_TYPE_FILLING, 'cutlet', 200),
    ])
    def test_ingredient_get_price(self, ingredient_type, name, price):
        """Тест метода get_price."""
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price

