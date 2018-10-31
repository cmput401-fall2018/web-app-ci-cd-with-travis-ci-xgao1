import unittest
from unittest.mock import patch, mock_open
from unittest import TestCase, mock
from service import Service

class ServiceTest(TestCase):

    def test_divide(self):
        service = Service()
        service.bad_random = mock.Mock(return_value = 5)
        value = service.divide(5)
        assert value == 1


    def test_absplus(self):
        service = Service()
        value = abs_plus(1)
        assert value == 2

        value = abs_plus(-3)
        assert value == 4

        value = abs_plus(0)
        assert value == 1

    def test_complicated(self):
        service = Service()
        service.bad_random = mock.Mock(return_value = 5)
        value = service.complicated_function(5)
        self.assertRaises(ZeroDivisionError,service.divide,0)

        service.divide = mock.Mock(return_value=4)
        return_val = service.complicated_function(2)
        assert return_val[0] == 2
        assert return_val[1] == 2.5
