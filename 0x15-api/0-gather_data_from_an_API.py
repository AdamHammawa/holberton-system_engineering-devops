#!/usr/bin/python3
""" Python script that uses rest api to fetch data """

if __name__ == "__main__":
    """ script that gets todos from an user id """
    import requests
    from sys import argv

    todos_List = []
    todos_Completed = []
    # Making sure the argument passed is an int
    employee_id = int(argv[1])
    employee_info = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}"
        .format(employee_id)).json()
    employee_name = employee_info['name']
    employee_todosList = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'
        .format(employee_id)).json()
    for todo in employee_todosList:
        todos_List.append(todo.get("completed"))
        if (todo.get("completed")):
            todos_Completed.append(todo.get("title"))
    print("Eployee {} is done with tasks({}/{}):"
          .format(employee_name, len(todos_Completed), len(todos_List)))
    for task in todos_Completed:
        print("\t {}".format(task))
