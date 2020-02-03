#!/usr/bin/python3
""" Python script that uses rest api to fetch data """

if __name__ == "__main__":
    """ script that gets todos from an user id """
    import requests
    import csv
    from sys import argv

    # Making sure the argument passed is an int
    employee_id = int(argv[1])
    employee_info = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)).json()
    employee_name = employee_info['name']
    employee_todosList = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(employee_id)).json()
    # writers a csv file now with #.csv as the file name
    with open("{}.csv".format(employee_id), "w") as f:
        row = csv.writer(f, delimiter=",", quoting=csv.QUOTE_ALL)
        for todo in employee_todosList:
            row.writerow([employee_id, employee_info.get("username"),
                          todo.get("completed"), todo.get("title")])
