#! /usr/bin/env python

# Define a class for S-Expressions, and for each type of expression.

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

