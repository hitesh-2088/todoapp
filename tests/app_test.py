import unittest
from unittest.mock import patch
from typing import Dict, Any, List
from utility.fetchapi import fetch_todo, get_even_todos

class TestTodoFunctions(unittest.TestCase):
    @patch('utility.fetchapi.requests.get')
    def test_fetch_todo(self, mock_get) -> None:
        expected_todo: Dict[str, Any] = {'userId': 1, 'id': 2, 'title': 'Mock Todo', 'completed': False}
        mock_get.return_value.json.return_value = expected_todo
        mock_get.return_value.status_code = 200
        todo: Dict[str, Any] = fetch_todo(2)
        self.assertEqual(todo, expected_todo)

    @patch('utility.fetchapi.fetch_todo')
    def test_get_even_todos(self, mock_fetch_todo) -> None:
        mock_todo: Dict[str, Any] = {'userId': 1, 'id': 2, 'title': 'Mock Todo', 'completed': False}
        mock_fetch_todo.side_effect = [mock_todo, mock_todo, mock_todo, mock_todo]  # Simulate 4 even todos
        todos: List[Dict[str, Any]] = get_even_todos(4)
        self.assertEqual(len(todos), 4)
