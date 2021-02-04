#!/usr/bin/env python

f = open('test.txt', 'w+')
f.write("testing\n")
f.write("file\n")
f.close()

for line in open('test.txt'):
    print(line)

f = open('test.txt', 'r')
line = f.readline()
print(line)
f.close()

f = open('test.txt', 'r')
line = f.readlines()
print(line)
f.close()

with open('test.txt') as file:
    line = file.readline()  # premiere ligne
    print(line)
    for l  in file:    # ligne suivante
        print(l)


