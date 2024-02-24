import requests
import sys

TODO_URL_TEMPLATE = "https://jsonplaceholder.typicode.com/todos/{}"

def fetch_todo(todo_id):
    url = TODO_URL_TEMPLATE.format(todo_id)
    try :
        response = requests.get(url)
        if response.status_code == 200 :
            return response.json()
    except:
        raise Exception('GET Request call failed')

def get_even_todos(num_todos):
    todos = []
    print('Todo list is getting fethched...')
    for i in range(2, num_todos*2+1, 2):
        todo = fetch_todo(i)
        if i % 2 == 0:
            todos.append(todo)
            sys.stdout.write('\r..')
        if len(todos) == num_todos:
            break
    return todos
