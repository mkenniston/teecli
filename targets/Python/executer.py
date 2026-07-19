#! /usr/bin/python

# This is a skeleton program to read ESE (encoded s-expression) data
# and create the actual s-expressions.  ESE is much easier for a
# machine to read than the original human-readable s-expressions.
 
import sys

class SE:
  pass

class Pair(SE):

  def __init__(self, left, right):
    self._left = left
    self._right = right

  def __str__(self):
    return "( " + str(self._left) + self.tail_str()

  def tail_str(self):
    tail = self._right
    if isinstance(tail, AtomNil):
      return " )"
    if isinstance(tail, Pair):
      return " " + str(tail._left) + tail.tail_str()
    return " . " + str(tail) + " )"

class Atom(SE):

  def __init__(self, value):
    self._value = value

  def __str__(self): 
    return str(self._value)

class AtomNil(Atom):

  def __init__(self):
    Atom.__init__(self, None)

  def __str__(self):
    return "()"

class AtomInt(Atom):

  def __init__(self, value):
    Atom.__init__(self, int(value))

class AtomFloat(Atom):

  def __init__(self, value):
    Atom.__init__(self, float(value))

class AtomStr(Atom):
  def __str__(self):
    return '"%s"' % self._value

class AtomSym(Atom):
  def __str__(self):
    return '%s' % self._value

class Reader:

  def is_white_space(self, c):
    return c in " \t\n\r\v"

  def read_one_token(self):
    # consume any leading whitespace
    char = " "
    while char and self.is_white_space(char):
      char = sys.stdin.read(1)
    # read one string of non-whitespace (unless quoted with \\)
    quoting = False
    token = ""
    while True:
      if not char:
        # hit EOF
        if token == "":
          return None
        return token
      if not quoting and char == "\\":
        quoting = True
      elif not quoting and self.is_white_space(char):
        return token
      else:
        token += char
        quoting = False
      char = sys.stdin.read(1)

  def read_one_expr(self):
    stack = []
    while True:
      token = self.read_one_token()
      if not token:
        if len(stack) == 0:
          return None
        raise Exception("premature EOF")
      if token == "E":
        if len(stack) != 1:
          raise Exception("not a valid end")
        return stack.pop()
  
      if token == "P":
        if len(stack) < 2:
          raise Exception("no pair to push")
        right = stack.pop()
        left = stack.pop()
        stack.append(Pair(left, right))
        continue
      if token == "N":
        stack.append(AtomNil())
        continue
  
      value = self.read_one_token()
      if not value:
        raise Exception("no value")
  
      if token == "I":
        stack.append(AtomInt(value))
      elif token == "F":
        stack.append(AtomFloat(value))
      elif token == "S":
        stack.append(AtomStr(value))
      elif token == "Y":
        stack.append(AtomSym(value))

class Executer:
  
  def execute(self, expr):
    print(expr)
   
def main():
  reader = Reader()
  executer = Executer()

  expr = reader.read_one_expr()
  while expr:
    executer.execute(expr)
    expr = reader.read_one_expr()

if __name__ == "__main__":
  main()

