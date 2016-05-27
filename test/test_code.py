from code import calculator

from unittest import TestCase
from unittest import mock

class MyTests(TestCase):

    def test_my_first_test(self):
        self.assertTrue(True)

    def test_proba(self):
        self.assertEqual(True, True)


class TestMyAddition(TestCase):

    def test_my_add_is_callable(self):
        calculator(3, 4)

    # def test_i_can_add_2_and_2(self):
    #     expected = 4
    #     result = add(2, 2)
    #     self.assertEqual(expected, result)
    #
    # def test_i_can_add_5_and_2(self):
    #     expected = 7
    #     result = add(5, 2)
    #     self.assertEqual(expected, result)

    # @mock.patch('code.parse_html')
    # def test__vmivmi(self, mock_parser):
    #     mock_parser.return_value = 0
    #     expected = 4
    #     result = add(4, 4)
    #     self.assertEqual(expected, result)

    def test__osszeadas1(self):
        expected = 9
        result = calculator(4,5)
        self.assertEqual(expected, result)

    def test__szorzas1(self):
        expected = 10
        result = calculator(2,5,'*')
        self.assertEqual(expected, result)

    def test__osztas1(self):
        expected = 4
        result = calculator(20, 5, ':')
        self.assertEqual(expected, result)

    def test__osztas2(self):
        expected = 0.25
        result = calculator(5,20,':')
        self.assertEqual(expected, result)

    def test__kivonas1(self):
        expected = 3
        result = calculator(5,2,'-')
        self.assertEqual(expected, result)

    def test__hiba1(self):
        expected = 'None'
        result = calculator(5,2,'')
        self.assertEqual(expected, result)

    def test__negyzet1(self):
        expected = 9
        result = calculator(3,2,'^')
        self.assertEqual(expected, result)

    def test__gyok1(self):
        expected = 3
        result = calculator(9, 1/2, '^')
        self.assertEqual(expected, result)