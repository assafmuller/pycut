from pycut import pycut
from pycut.tests import base as tests_base


class PycutTestCase(tests_base.BaseTestCase):
    def test_single_field(self):
        value = 'some_file.json.00000'
        delimiter = '.'

        self.assertEqual('some_file', pycut.cut(value, '1', delimiter))
        self.assertEqual('json', pycut.cut(value, '2', delimiter))
        self.assertEqual('00000', pycut.cut(value, '3', delimiter))

    def test_field_range(self):
        pass
