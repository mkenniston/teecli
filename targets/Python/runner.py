#! /usr/bin/python

# This is a skeleton program to read ESE (encoded s-expression) data
# and create the actual s-expressions.  ESE is much easier for a
# machine to read than the original human-readable s-expressions.
 
from Reader import *
from Executer import *

def main():
  reader = Reader()
  executer = Executer()

  expr = reader.read_one_expr()
  while expr:
    executer.execute(expr)
    expr = reader.read_one_expr()

if __name__ == "__main__":
  main()

