import pytest

from praktikum.bun import Bun


class TestBun:
    """Тесты для класса Bun."""

    @pytest.mark.parametrize('name,price', [
        ('black bun', 100),
        ('white bun', 200),
        ('red bun', 300),
        ('sesame bun', 150),
    ])
    def test_bun_init(self, name, price):
        """Тест инициализации булочки с различными параметрами."""
        bun = Bun(name, price)
        assert bun.name == name
        assert bun.price == price

    @pytest.mark.parametrize('name,price', [
        ('black bun', 100),
        ('white bun', 200),
        ('red bun', 300),
    ])
    def test_bun_get_name(self, name, price):
        """Тест метода get_name."""
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize('name,price', [
        ('black bun', 100),
        ('white bun', 200),
        ('red bun', 300),
    ])
    def test_bun_get_price(self, name, price):
        """Тест метода get_price."""
        bun = Bun(name, price)
        assert bun.get_price() == price

