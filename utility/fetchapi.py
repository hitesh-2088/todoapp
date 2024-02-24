import requests
import sys
from typing import List, Dict, Any

TODO_URL_TEMPLATE: str = "https://jsonplaceholder.typicode.com/todos/{}"

def fetch_todo(todo_id: int) -> Dict[str, Any]:
    url: str = TODO_URL_TEMPLATE.format(todo_id)
    try:
        response: requests.Response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except Exception as e:
        raise Exception('GET Request call failed') from e

def get_even_todos(num_todos: int) -> List[Dict[str, Any]]:
    todos: List[Dict[str, Any]] = []
    print('Todo list is getting fethched...')
    for i in range(2, num_todos*2 + 1, 2):
        todo: Dict[str, Any] = fetch_todo(i)
        if i % 2 == 0:
            todos.append(todo)
            sys.stdout.write('..\r')
        if len(todos) == num_todos:
            break
    return todos
