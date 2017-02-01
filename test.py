from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import unittest
from undict import undict

class UndictTestCase(unittest.TestCase):
  def test_primitive_type(self):
    self.assertEqual(1.0, undict(1.0))
    self.assertEqual(10, undict(10))
    self.assertEqual('Hello', undict('Hello'))

  def test_simple_dict(self):
    d = {
      'int_key': 1,
      'float_key': 23.33,
      'string_key': 'Whatsup',
      'list_key': [22, 33.3],
    }
    obj = undict(d)
    self.assertEqual(obj.int_key, d['int_key'])
    self.assertEqual(obj.float_key, d['float_key'])
    self.assertEqual(obj.string_key, d['string_key'])
    self.assertEqual(obj.list_key, d['list_key'])

  def test_simple_list(self):
    l = [1.0, 'Sup', 222]
    self.assertEqual(l, undict(l))

  def test_nested_struct(self):
    d = {
      'list_key': [
        {'int_key': 1},
        {'string_key': 'hello'},
      ],
      'dict_key': {
        'float_key': 22.2,
      },
    }
    obj = undict(d)
    self.assertEqual(obj.list_key[0].int_key, d['list_key'][0]['int_key'])
    self.assertEqual(obj.list_key[1].string_key, d['list_key'][1]['string_key'])
    self.assertEqual(obj.dict_key.float_key, d['dict_key']['float_key'])

  def test_get_raw_dict(self):
    d = {
      'int_key': 1,
      'float_key': 23.33,
      'string_key': 'Whatsup',
      'list_key': [22, 33.3],
    }
    self.assertEqual(undict(d).to_dict(), d)

  def test_modification(self):
    init_dict = {'key': 'value'}
    obj = undict(init_dict)
    obj.test_key = {'int_key': 1}
    self.assertEqual(obj.test_key.int_key, 1)


if __name__ == '__main__':
  unittest.main()
