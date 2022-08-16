def counter(func):
    # Decorator counting funcstion calls?
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        res = func(*args, **kwargs)
        print("{0} была вызвана: {1}x".format(func.__name__, wrapper.count))
        return res
    wrapper.count = 0
    return wrapper

def output():
    # Name the output
    a = [1, 2]
    b = a
    a.append(3)
    print(a, b)

    def foo(a, b=[]):
        b.append(a)
    foo(1)
    foo(2)
    print(foo(3))

# Объединить dict
def unite_dict(dict_a, dict_b):
    res = {**dict_a, **dict_b}
    return res

# Удалить повторяющиеся элементы в списке
def remove_duplicates(my_list):
    list(set(my_list))

# контекст менеджер with
# with with
class with_manager():
    def with_with():
        # __enter__ - момент входа в контекст
        c return
        __exit__
        # сделан для замены try except
        # close тоже критическая функция
        with open('') as f:
            f.write('')

    def without_with():
        # without `with`
        file = open('')
        try:
            file.write('')
        finally:
            file.close()

# yield
# вызвать генератор после елда, получить значение елда
def gen():
    for i in range(10):
        a = yield i

# counting the number of every character of a given text file.
def count_characters():
    import collections
    import pprint
    with open("sample_file.txt", 'r') as data:
    count_data = collections.Counter(data.read().upper())
    count_value = pprint.pformat(count_data)

# add two integers >0 without using the plus
def add_nums(num1, num2):
   while num2 != 0:
       data = num1 & num2
       num1 = num1 ^ num2
       num2 = data << 1
   return num1
print(add_nums(2, 10))

