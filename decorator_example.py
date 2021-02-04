import time
import functools

registry = []
def register(func):
    print('running register(%s)' % func)
    registry.append(func)
    return func


@register
def f1():
    print('running f1()')


@register
def f2():
    print('running f2()')

def f3():
    print('running f3()')


def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked


@clock
def snooze(seconds):
    time.sleep(seconds)


@clock
def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)


@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)

@functools.lru_cache()
@clock
def fibonacci2(n):
    if n < 2:
        return n
    return fibonacci2(n-2) + fibonacci2(n-1)



def main():
    print('running main()')

    print('registry ->', registry)
    f1()
    f2()
    f3()

    snooze(.123)
    factorial(6)
    print("\n")
    print(fibonacci(6))
    # fibonnaci(1) est appele 8 fois
    print("\n")
    print(fibonacci2(6))


if __name__ == '__main__':
    main()