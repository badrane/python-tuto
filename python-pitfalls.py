#!/usr/bin/env python

def some_func(args=[]):
    args.append("data")

some_func()
print(some_func.__defaults__)

some_func()
print(some_func.__defaults__)

some_func()
print(some_func.__defaults__)

# Better

def some_func(args=None):
    if args is None:
        args = []
    args.append("data")
    return args

a = some_func()
print(some_func.__defaults__)
print(a)

a = some_func()
print(some_func.__defaults__)
print(a)


a = some_func()
print(some_func.__defaults__)
print(a)
