from collections import namedtuple
import csv

Pair = namedtuple("Pair", ("x", "y"))

def row_iter(source):
    return csv.reader(source, delimiter="\t")

def head_split_fixed(row_iter):
    title= next(row_iter)
    print(title)
    heading= next(row_iter)
    print(heading)
    columns= next(row_iter)
    print(columns)
    return row_iter

def series(n, row_iter):
    for row in row_iter:
        yield Pair(*row[n*2:n*2+2])

with open("anscombe_quartet.csv") as source:
    data       = tuple(head_split_fixed(row_iter(source)))
    sample_I   = tuple(series(0,data))
    sample_II  = tuple(series(1, data))
    sample_III = tuple(series(2,data))
    sample_IV  = tuple(series(3,data))

#---- controle --------------------------------
for value in sample_I:
    print("{} {}".format(value.x,value.y))


