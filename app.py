import sys
from utility import fetchapi

def print_todos(todos):
    for todo in todos:
        print("Title:", todo['title'])
        print("Completed:", todo['completed'])
        print()

def main():
    num_todos = int(sys.argv[1]) if len(sys.argv) > 1 else 20
    even_todos = fetchapi.get_even_todos(num_todos)
    print_todos(even_todos)

if __name__ == "__main__":
    main()
