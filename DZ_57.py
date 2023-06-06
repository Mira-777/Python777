from jinja2 import Template

html = """
{%- macro text_input(name, placeholder, type='text') -%}
    <input type="{{type}}" name="{{ name }}" placeholder="{{ placeholder }}">
{%- endmacro -%}
<p>{{ text_input('firsname', 'Имя') }}</p>
<p>{{ text_input('lastname', 'Фамилия') }}</p>
<p>{{ text_input('address', 'Адрес') }}</p>
<p>{{ text_input('phone','Телефон','tel') }}</p>
<p>{{ text_input('email', 'Почта','email') }}</p>
"""

tm = Template(html)
msg = tm.render()

print(msg)