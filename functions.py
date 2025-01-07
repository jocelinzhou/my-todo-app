FILEPATH = 'todos.txt'

def get_todos(filepath = FILEPATH):
    with open(FILEPATH,'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg):
    with open(FILEPATH,'w') as file:
        file.writelines(todos_arg)
