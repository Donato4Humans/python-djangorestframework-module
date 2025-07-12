from unittest import TestCase
from unittest.mock import MagicMock, patch

from ..service import calc, math


class CalcTestCase(TestCase):
    # @patch('apps.pizza.service.cos')# if you need test imports that can`t be executed while testing(cash operations or other)
    @patch.object(math, 'cos')
    def test_plus(self, mock_cos:MagicMock):
        mock_cos.return_value = 55# you specify here value that must be returned from func that can`t be executed
        res = calc(1,2, "+")
        self.assertEqual(res,57)

    def test_minus(self):
        res = calc(1,2, "-")
        self.assertEqual(res,-1)

    def test_multiply(self):
        res = calc(1,2, "*")
        self.assertEqual(res,2)