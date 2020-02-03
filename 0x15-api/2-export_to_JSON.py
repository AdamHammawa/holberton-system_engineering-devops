#!/usr/bin/python3
""" Python script that uses rest api to fetch data """

if __name__ == "__main__":
    """ script that gets todos from an user id """
    import requests
    import json
    from sys import argv

    # Making sure the argument passed is an int
    employee_id = int(argv[1])
    employee_info = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)).json()
    employee_name = employee_info['name']
    employee_todosList = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(employee_id)).json()
    array = []
    for todo in employee_todosList:
        tmp = {}
        tmp["task"] = todo.get("title")
        tmp["completed"] = todo.get("completed")
        tmp["username"] = employee_info.get("username")
        array.append(tmp)

    jsonstatham = {}
    jsonstatham[employee_id] = array
    with open("{}.json".format(employee_id), "w") as f:
        json.dump(jsonstatham, f)
