# -- coding:utf-8 --
import pytest
import allure


@allure.feature("测试Dome")
class TestClass:
    @allure.story("测试用例 1")
    def test_one(self):
        x = "hello"
        assert 'h' in x

    @allure.story("测试用例 2")
    def test_two(self):
        x = "test"
        assert hasattr(x, 'check')
