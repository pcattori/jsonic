from __future__ import absolute_import
import jsonic
import unittest

TEST_RECORDS = [
    {'a': 1, 'b': 3, 'c': 'V'},
    {'a': 1, 'b': 4, 'c': 'W'},
    {'a': 1, 'b': 5, 'c': 'X'},
    {'a': 2, 'b': 6, 'c': 'Y'},
    {'a': 2, 'b': 7, 'c': 'Z'}
]

class OpsTest(unittest.TestCase):

    def test_group_by(self):
        group_by_a = jsonic.group_by(
            iter(TEST_RECORDS), lambda r: r['a'], value=lambda r: r['b']
        )
        self.assertEqual(sorted(group_by_a[1]), [3, 4, 5])
        self.assertEqual(sorted(group_by_a[2]), [6, 7])

    def test_index(self):
        index = jsonic.index(TEST_RECORDS, lambda r: r['b'], value=lambda r: r['c'])
        self.assertEqual(index, {3: 'V', 4: 'W', 5: 'X', 6: 'Y', 7: 'Z'})

if __name__ == '__main__':
    unittest.main()
