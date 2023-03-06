import re


def validate_password(name):
    return re.findall(r'[A-Za-z_0-9-@]{8,16}', name)


print(validate_password('my_p@ss0rd'))