from jinja2 import Environment, FileSystemLoader

persons = [
    {'name': 'Иванов', 'year': 15, 'weight': 48},
    {'name': 'Берлинский', 'year': 14, 'weight': 50},
    {'name': 'Рощупкин', 'year': 14, 'weight': 53},

]

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

tm = env.get_template('main.html')
msg = tm.render(users=persons)

print(msg)