import functools

def detail(name, age):
    return  name, age

func = functools.partial(detail, 'xiaoming', 12)
print func()