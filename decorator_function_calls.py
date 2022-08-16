# Decorator counts function calls
def dec_counter(func):
  def wrapper(*args, **kwargs):
    wrapper.count += 1
    print('calls:', wrapper.count)
    return func
  wrapper.count = 0
  return wrapper
@dec_counter
def random_func():
  print('wheee')
random_func()
random_func()
random_func()
random_func()

# What we will see
a = [1, 2]
b = a
a.append(3)
print(a, b)