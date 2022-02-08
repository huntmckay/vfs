import requests
#test just the backend without frontend

def query():
    response = requests.get('http://localhost:5000/todo_db')
    print(response.json())

query()

# test adding a new item

data = {'content':'add a new todo ', 'done':False}
response = requests.post('http://localhost:5000/todo_db', json= data)
query()

# update the old item
data = {'content':'change a todo ', 'done':True, 'id':1}
response = requests.post('http://localhost:5000/todo_db', json= data)
query()

# remove item
data = {'delete': True, 'id':2}
response = requests.post('http://localhost:5000/todo_db', json= data)
query()
