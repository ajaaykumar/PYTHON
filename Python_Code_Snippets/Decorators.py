
def debug(func):
    def wrapper(*args,**kwargs):
        print(f"Calling {func.__name__} with {args} and {kwargs}")
        result = func(*args,**kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@debug
def add(a,b):
    return a+b

# print(add(9999,1))

# Calling add with (9999, 1) and {}
# add returned 10000
# 10000


def trace(func):
    """A decorator that traces function calls."""
    def wrapper(*args,**kwargs):
        print(f"Trace: calling {func.__name__}() with {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Trace: {func.__name__}() returned {result}")
        return result
    return wrapper

@trace
def compute_area(length,width):
    return length*width

area = compute_area(3.0, 4.5)
print(area)


