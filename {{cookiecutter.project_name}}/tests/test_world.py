import io
import unittest

from unittest.mock import patch
from {{ cookiecutter.project_name }}.world import say_hello


class TestWorld(unittest.TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_should_say_hello(self, mock_stdout):
        say_hello()
        self.assertEqual('hello world\n', mock_stdout.getvalue())


if __name__ == '__main__':
    unittest.main()
