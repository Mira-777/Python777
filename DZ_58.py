from jinja2 import Template

catalogs = [
    #{'id': "/news", 'name': 'Новости'},
    {'id': "/about", 'name': 'О компании'},
    {'id': "/shop", 'name': 'Магазин'},
    {'id': "/contact", 'name': 'Контакты'},
]

class active:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def get_name(self):
        return self.id
    def get_age(self):
        return self.name

p = active("/index", "Главная")


link = """<ul>
<li><a href="/index" class= "active">Главная</a></li>
{% for c in catalogs -%}
<li><a href="{{ c['id'] }}">{{ c.name }}</a></li>
{% endfor -%}
</ul>

"""

tm = Template(link)
msg = tm.render(catalogs=catalogs)
print(msg)