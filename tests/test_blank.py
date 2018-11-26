from unittest import TestCase
from mycode import fun_tested, fun_half_tested


class TestBlank(TestCase):
    def test_1(self):
        self.assertTrue(fun_tested())

    def test_2(self):
        self.assertTrue(fun_half_tested(False))
