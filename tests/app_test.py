import unittest
from unittest.mock import patch
from utility.fetchapi import fetch_todo, get_even_todos

class TestTodoFunctions(unittest.TestCase):
    @patch('utility.fetchapi.requests.get')
    def test_fetch_todo(self, mock_get):
        expected_todo = {'userId': 1, 'id': 2, 'title': 'Mock Todo', 'completed': False}
        mock_get.return_value.json.return_value = expected_todo
        mock_get.return_value.status_code = 200
        todo = fetch_todo(2)
        self.assertEqual(todo, expected_todo)

    @patch('utility.fetchapi.fetch_todo')
    def test_get_even_todos(self, mock_fetch_todo):
        mock_todo = {'userId': 1, 'id': 2, 'title': 'Mock Todo', 'completed': False}
        mock_fetch_todo.side_effect = [mock_todo, mock_todo, mock_todo, mock_todo]  # Simulate 4 even todos
        todos = get_even_todos(4)
        self.assertEqual(len(todos), 4)
