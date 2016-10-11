from __future__ import absolute_import, unicode_literals

import json
import jsonic
import tempfile
import unittest

TEST_RECORDS = [
    {'a': 1, 'b': 'B'},
    {'a': 'A', 'b': 2}
]

TEST_NEWLINE_JSON = '''{"a": 1, "b": "B"}
{"a": "A", "b": 2}'''

class IoTest(unittest.TestCase):

    def test_stream_file(self):
        with tempfile.TemporaryFile('w+') as f:
            f.write(TEST_NEWLINE_JSON)
            f.flush()
            f.seek(0)
            self.assertEqual(list(jsonic.stream_file(f)), TEST_RECORDS)

    def test_write_file(self):
        with tempfile.TemporaryFile('w+') as f:
            jsonic.write_file(iter(TEST_RECORDS), f)
            f.seek(0)
            written = [json.loads(line) for line in f]
            self.assertEqual(written, TEST_RECORDS)

    def test_stream_filepath(self):
        with tempfile.NamedTemporaryFile('w+') as f:
            f.write(TEST_NEWLINE_JSON)
            f.flush()
            self.assertEqual(list(jsonic.stream_filepath(f.name)), TEST_RECORDS)

    def test_write_filepath(self):
        with tempfile.NamedTemporaryFile('w+') as f:
            jsonic.write_filepath(iter(TEST_RECORDS), f.name)
            f.seek(0)
            written = [json.loads(line) for line in f]
            self.assertEqual(written, TEST_RECORDS)

if __name__ == '__main__':
    unittest.main()
