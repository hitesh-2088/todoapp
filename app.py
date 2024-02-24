import sys
from typing import List, Dict, Any
from utility import fetchapi

def print_todos(todos: List[Dict[str, Any]]) -> None:
    for todo in todos:
        print("Title:", todo['title'])
        print("Completed:", todo['completed'])
        print()

def main() -> None:
    num_todos: int = int(sys.argv[1]) if len(sys.argv) > 1 else 20
    even_todos: List[Dict[str, Any]] = fetchapi.get_even_todos(num_todos)
    print_todos(even_todos)

if __name__ == "__main__":
    main()
