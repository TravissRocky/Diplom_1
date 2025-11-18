from unittest.mock import Mock, patch

import pytest

from praktikum.bun import Bun
from praktikum.database import Database
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:
    """Тесты для класса Database."""

    def test_database_init(self):
        """Тест инициализации базы данных."""
        database = Database()
        assert len(database.buns) == 3
        assert len(database.ingredients) == 6
        assert isinstance(database.buns[0], Bun)
        assert isinstance(database.ingredients[0], Ingredient)

    def test_database_available_buns(self):
        """Тест метода available_buns."""
        database = Database()
        buns = database.available_buns()
        assert len(buns) == 3
        assert all(isinstance(bun, Bun) for bun in buns)
        assert buns[0].get_name() == 'black bun'
        assert buns[1].get_name() == 'white bun'
        assert buns[2].get_name() == 'red bun'

    def test_database_available_ingredients(self):
        """Тест метода available_ingredients."""
        database = Database()
        ingredients = database.available_ingredients()
        assert len(ingredients) == 6
        assert all(isinstance(ingredient, Ingredient) for ingredient in ingredients)
        # Проверяем, что есть соусы и начинки
        sauce_count = sum(1 for ing in ingredients if ing.get_type() == INGREDIENT_TYPE_SAUCE)
        filling_count = sum(1 for ing in ingredients if ing.get_type() == INGREDIENT_TYPE_FILLING)
        assert sauce_count == 3
        assert filling_count == 3

    @patch('praktikum.database.Bun')
    @patch('praktikum.database.Ingredient')
    def test_database_init_with_mocks(self, mock_ingredient, mock_bun):
        """Тест инициализации базы данных с использованием моков."""
        mock_bun_instance = Mock()
        mock_bun.return_value = mock_bun_instance
        
        mock_ingredient_instance = Mock()
        mock_ingredient.return_value = mock_ingredient_instance
        
        database = Database()
        
        # Проверяем, что Bun был вызван 3 раза
        assert mock_bun.call_count == 3
        # Проверяем, что Ingredient был вызван 6 раз
        assert mock_ingredient.call_count == 6
        assert len(database.buns) == 3
        assert len(database.ingredients) == 6

