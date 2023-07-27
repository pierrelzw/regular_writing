
def my_func(a, b):
    x = a + b
    y = x * x
    z = y * 2
    w = z * 2
    return w

# return intermediate results with hook mechanism, without modifying my_func or its implmentation

# hook mechanism
def hook(func, hook_func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        hook_func(*args, **kwargs, **result)
        return result
    return wrapper

# hook function
def hook_func(*args, **kwargs):
    print(args, kwargs)

# hook my_func
my_func = hook(my_func, hook_func)

# call my_func
my_func(1, 2)

